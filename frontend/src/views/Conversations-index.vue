<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const tab = ref("");
const splitterModel = ref(20);
const conversationItems = ref([]);

const fetchConversationItems = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/conversation-items/");
  conversationItems.value = res.data;
};
const submitMessage = async () => {
  // Intentionally empty (for now)
};

onMounted(() => {
  fetchConversationItems();
});
</script>

<template>
  <div>
    <q-splitter v-model="splitterModel" style="height: 30em">
      <template v-slot:before>
        <q-tabs v-model="tab" vertical class="text-teal">
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
                <q-btn label="Submit" type="submit" color="primary" />
              </div>
            </q-form>
          </q-tab-panel>
        </q-tab-panels>
      </template>
    </q-splitter>
  </div>

  <div class="text-left q-my-md">
    <q-btn color="primary" :to="{ name: 'conversations.create' }">
      <q-icon left size="xl" name="mdi-plus-box" />
      <div>Ajouter</div>
    </q-btn>
  </div>
</template>
