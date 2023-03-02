<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const conversationItems = ref([]);

const fetchConversationItems = async () => {
  const res = await axios.get("http://localhost:8000/api/conversation-items/");
  conversationItems.value = res.data;
};

onMounted(() => {
  fetchConversationItems();
});
</script>

<template>
  <div>
    <div
      class="my-card q-mt-md"
      v-for="(item, index) in conversationItems"
      :key="index"
    >
      <q-card-section class="bg-grey-8 text-white">
        <div class="text-h6">{{ item.name }}</div>
      </q-card-section>
    </div>
  </div>

  <div class="text-left q-my-md">
    <q-btn color="primary" :to="{ name: 'conversations.create' }">
      <q-icon left size="xl" name="mdi-plus-box" />
      <div>Ajouter</div>
    </q-btn>
  </div>
</template>
