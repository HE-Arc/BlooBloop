<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import AxiosService from "../../utils/AxiosService.mjs";
import moment from "moment";

import "@/assets/shake.css";

const API_URL = import.meta.env.VITE_API_URL;
const WS_HOST = import.meta.env.VITE_WEBSOCKET_HOST;

const route = useRoute();
const router = useRouter();
const errors = ref(null);

const loggedUserId = ref(-1);
const message = ref("");
const shake = ref(false);

const tab = ref("");
const splitterModel = ref(20);

const messageItems = ref([]);
const conversationItems = ref([]);

let webSocket = null;

const fetchConversationItems = async () => {
  await AxiosService.GET(`${API_URL}conversation-items/profile/`).then(
    (response) => {
      conversationItems.value = response.data;
    }
  );
};

const fetchMessages = async (id) => {
  const response = await AxiosService.GET(`${API_URL}message-items/`);

  messageItems.value = response.data.filter(
    (msg) => msg.conversation.id === id
  );
};

const startWebSocket = async (id) => {
  webSocket = new WebSocket("ws://" + WS_HOST + "/ws/chat/" + id + "/");

  // receive message
  webSocket.onmessage = () => {
    fetchMessages(id);

    new Audio("/tunes/BlooBloop.mp3").play();
  };
};

const closeWebSocket = async () => {
  if (webSocket != null) {
    webSocket.close();
    webSocket = null;
  }
};

const startFetchingMessages = async (id) => {
  await closeWebSocket();

  startWebSocket(id);
  fetchMessages(id);
};

const submitMessage = async (index) => {
  const result = await AxiosService.POST(
    `${API_URL}message-items/custom-post/`,
    {
      content: message.value,
      conversation_id: index,
    }
  );

  if (result.status == 201) {
    message.value = "";
    new Audio("/tunes/BlooBloop.mp3").play();

    router.push({
      path: "/conversations",
    });
  } else {
    new Audio("/tunes/wrong.mp3").play();
    shake.value = true;
    setTimeout(() => {
      shake.value = false;
    }, 820);
  }

  webSocket.send(
    JSON.stringify({
      message: message.value,
    })
  );

  message.value = "";

  fetchMessages(index);
};

const remove = async (index) => {
  await AxiosService.DELETE(`${API_URL}conversation-items/${index}/`);

  await fetchConversationItems();
};

onMounted(async () => {
  let jsonUser = localStorage.getItem("user");

  if (jsonUser != null) {
    let user = JSON.parse(jsonUser);
    loggedUserId.value = user.id;

    fetchConversationItems();
  }

  // ! TODO : FIX not closing web socket when leaving conversation page because doesn't pass by the listener
  watch(
    () => route.path,
    () => {
      console.log("ON QUITTE LES CONV !!!");
      closeWebSocket();
    }
  );
});
</script>

<template>
  <main>
    <div class="q-ma-lg">
      <h3 class="text-center">Conversations</h3>
      <q-splitter v-model="splitterModel">
        <template v-slot:before>
          <q-tabs v-model="tab" vertical class="text-primary">
            <q-tab
              v-for="(item, index) in conversationItems"
              :key="index"
              :name="item.name"
              :label="item.name"
              @click="() => startFetchingMessages(item.id)"
            />
          </q-tabs>
        </template>

        <template v-slot:after>
          <q-tab-panels
            v-model="tab"
            animated
            swipeable
            vertical
            transition-prev="jump-up"
            transition-next="jump-up"
          >
            <q-tab-panel
              v-for="(item, index) in conversationItems"
              :key="index"
              :name="item.name"
            >
              <div class="text-h4 q-mb-md">{{ item.name }}</div>
              <p>
                <span
                  v-for="(user, index) in item.users"
                  :key="index"
                  :name="user.user.username"
                >
                  {{ user.user.username }},
                </span>
              </p>
              <div class="q-mb-md" v-for="m in messageItems" :key="m.id">
                <q-chat-message
                  :name="m.profile.user.username"
                  :text="[m.content]"
                  :stamp="moment(m.created_at).format('LLLL')"
                  :sent="m.profile.id === loggedUserId"
                  :text-color="
                    m.profile.id === loggedUserId ? 'black' : 'white'
                  "
                  :bg-color="
                    m.profile.id === loggedUserId ? 'green' : 'primary' //amber-7
                  "
                />
              </div>
              <q-form @submit="(_$event) => submitMessage(item.id)">
                <q-input
                  :class="{ 'apply-shake': shake }"
                  filled
                  v-model="message"
                  label="Enter a message"
                />
                <div class="q-mt-md">
                  <q-btn label="Send" type="submit" color="primary" />
                </div>
              </q-form>
              <div class="q-mt-md row justify-end">
                <q-btn color="negative" @click="remove(item.id)">Delete</q-btn>
                <q-btn class="q-ml-md" color="warning">
                  <router-link :to="`conversations/${item.id}`"
                    >Update</router-link
                  >
                </q-btn>
              </div>
            </q-tab-panel>
          </q-tab-panels>
        </template>
      </q-splitter>
    </div>

    <div class="row justify-center q-mt-lg">
      <q-btn round color="primary" :to="{ name: 'conversations.create' }">
        <q-icon size="sm" name="mdi-plus-box" />
      </q-btn>
    </div>
  </main>
</template>

<style scoped>
a {
  text-decoration: none;
}
a:visited {
  color: white;
}
</style>
