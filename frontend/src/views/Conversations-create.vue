<script setup>
import axios from "axios";
import { ref } from "vue";

const name = ref("");

const submit = async () => {
  try {
    errors.value = null;
    success.value = false;
    await axios.post("http://localhost:8000/api/conversation-items/", {
      name: name.value,
    });
    success.value = true;
    window.location.href = "http://localhost:5173/conversations";
  } catch (error) {
    errors.value = error.response.data;
  }
};

const success = ref(false);
const errors = ref(null);
</script>

<template>
  <main>
    <div class="q-mx-auto" style="max-width: 50%">
      <h3>New Conversation</h3>
      <q-form @submit="submit" class="q-gutter-md">
        <q-input
          filled
          v-model="name"
          label="Conversation name"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Name is missing']"
        />
        <div class="row justify-center">
          <q-btn label="Create" type="submit" color="primary" />
        </div>
      </q-form>
    </div>
  </main>
</template>
