<script setup>
import axios from "axios";
import { ref } from "vue";

const username = ref("");
const email = ref("");
const password = ref("");

const success = ref(false);
const errors = ref(null);

const submit = async () => {
  try {
    success.value = false;
    errors.value = null;

    await axios.post("http://127.0.0.1:8000/api/users/", {
      username: username.value,
      email: email.value,
      password: password.value,
    });
    success.value = true;
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
      <label for="email">Email </label>
      <input type="email" v-model="email" required />
    </div>
    <div class="form-control">
      <label for="password">Password </label>
      <input type="password" v-model="password" required />
    </div>
    <button type="submit">Submit</button>
  </form>
</template>
