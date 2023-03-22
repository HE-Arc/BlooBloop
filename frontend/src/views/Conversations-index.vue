<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const API_URL = import.meta.env.VITE_API_URL;

const tab = ref("");
const splitterModel = ref(20);
const conversationItems = ref([]);

const fetchConversationItems = async () => {
  const res = await axios.get(API_URL + "conversation-items");
  conversationItems.value = res.data;
};
const submitMessage = async () => {
  // Intentionally empty (for now)
};

const remove = async (index) => {
  await axios.delete(API_URL + `conversation-items/${index}`);

  await fetchConversationItems();
};

onMounted(() => {
  fetchConversationItems();
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
                This is where we would put our message history.. if we had one!
              </p>
              <q-form @submit="submitMessage" class="q-gutter-md">
                <q-input
                  filled
                  v-model="name"
                  label="Enter message.. (not functional)"
                />
                <div>
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
