<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import AxiosService from "../../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;
const router = useRouter();
const errors = ref(null);

const loggedUserId = ref(-1);
const message = ref("");

const tab = ref("");
const splitterModel = ref(20);

const messageItems = ref([]);
const conversationItems = ref([]);

const fetchConversationItems = async () => {
  await AxiosService.GET(`${API_URL}conversation-items/profile/`).then(
    (response) => {
      conversationItems.value = response.data;
    }
  );
};

const fetchMessages = async (index) => {
  await AxiosService.GET(`${API_URL}message-items/`).then((response) => {
    messageItems.value = response.data.filter(
      (msg) => msg.conversation.id === index
    );
  });
};

const submitMessage = async (index) => {
  errors.value = null;

  await AxiosService.POST(`${API_URL}message-items/custom-post/`, {
    content: message.value,
    conversation_id: index,
  }).then(
    () => {
      router.push({
        path: "/conversations",
      });
    },
    (error) => {
      errors.value = error.response.data;
    }
  );
};

const remove = async (index) => {
  await AxiosService.DELETE(`${API_URL}conversation-items/${index}/`);

  await fetchConversationItems();
};

onMounted(async () => {
  await AxiosService.GET(`${API_URL}profile-items/logged-user-id/`).then(
    (response) => {
      loggedUserId.value = response.data;
      fetchConversationItems();
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
              @click="() => fetchMessages(item.id)"
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
              <div
                class="q-mb-md"
                v-for="message in messageItems"
                :key="message.id"
              >
                <q-chat-message
                  :name="message.profile.user.username"
                  :text="[message.content]"
                  :stamp="message.created_at"
                  :sent="message.profile.id === loggedUserId"
                  :text-color="
                    message.profile.id === loggedUserId ? 'black' : 'white'
                  "
                  :bg-color="
                    message.profile.id === loggedUserId ? 'green' : 'primary' //amber-7
                  "
                />
              </div>
              <q-form @submit="(_$event) => submitMessage(item.id)">
                <q-input filled v-model="message" label="Enter a message" />
                <div class="q-mt-md">
                  <q-btn label="Send" type="submit" color="primary" />
                </div>
              </q-form>
              <div class="q-mt-md row justify-end">
                <q-btn color="negative" @click="remove(item.id)">Delete</q-btn>
                <q-btn class="q-ml-md" color="warning">Update</q-btn>
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
