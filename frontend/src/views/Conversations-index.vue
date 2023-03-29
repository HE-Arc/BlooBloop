<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const API_URL = import.meta.env.VITE_API_URL;

const message = ref("");

const tab = ref("");
const splitterModel = ref(20);

const messageItems = ref([]);
const conversationItems = ref([]);

const fetchConversationItems = async () => {
  const res = await axios.get(API_URL + "conversation-items/");
  conversationItems.value = res.data;
};

const fetchMessages = async (index) => {
  const res = await axios.get(API_URL + "message-items/");

  messageItems.value = res.data.filter((msg) => msg.conversation.id === index);
};

const submitMessage = async () => {
  try {
    // TODO: Terminer avec les users
    // TODO: Améliorer la disposition du chat une fois que les utilisateurs seront connectés
    errors.value = null;
    success.value = false;

    await axios.post(API_URL + "message-items/", {
      content: message.value,
    });

    success.value = true;
  } catch (error) {
    console.log(error);
    errors.value = error.response.data;
  }
};

const remove = async (index) => {
  await axios.delete(API_URL + `conversation-items/${index}/`);

  await fetchConversationItems();
};

onMounted(() => {
  fetchConversationItems();
});

const success = ref(false);
const errors = ref(null);
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
              <p
                v-for="(user, index) in item.users"
                :key="index"
                :name="user.user.username"
              >
                {{ user.user.username }}
              </p>
              <div
                class="q-mb-md"
                v-for="message in messageItems"
                :key="message.id"
              >
                <q-chat-message :name="message.profile.user.username">
                  <div>{{ message.content }}</div>
                </q-chat-message>
              </div>
              <q-form @submit="submitMessage">
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
