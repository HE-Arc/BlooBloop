<script setup>
import axios from "axios";
import { ref } from "vue";

const username = ref("");
const password = ref("");

const errors = ref(null);

const submit = async () => {
  try {
    errors.value = null;

    await axios.post("http://127.0.0.1:8000/api/users/login", {
      username: username.value,
      password: password.value,
    });
  } catch (error) {
    errors.value = error.response.data;
  }
};
</script>

<template>
  {{ errors }}

  <form @submit.prevent="submit">
    <div class="form-control">
      <label for="username">Username </label>
      <input type="text" v-model="username" required />
    </div>
    <div class="form-control">
      <label for="password">Password </label>
      <input type="password" v-model="password" required />
    </div>
    <button type="submit">Login</button>
  </form>
</template>
