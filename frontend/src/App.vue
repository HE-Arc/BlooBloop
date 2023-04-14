<script setup>
import { ref, onMounted } from "vue";
import { RouterView } from "vue-router";
import AxiosService from "../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;

const userLogged = ref(false);
const username = ref("");

const isUserLogged = async () => {
  const res = await AxiosService.GET(API_URL + "profile-items/authenticated/");
  return res.data;
};

const fetchUsername = async () => {
  const user = await AxiosService.GET(
    API_URL + "profile-items/logged-username/"
  );

  username.value = user.data;
};

onMounted(async () => {
  userLogged.value = await isUserLogged();
  await fetchUsername();
});
</script>

<template>
  <header>
    <div class="q-pa-md">
      <q-toolbar class="bg-primary text-white q-my-md shadow-2">
        <q-btn stretch flat label="BlooBloop" to="/" />

        <q-space />

        <p v-if="userLogged == true" class="text-h6" style="margin: 0px">
          {{ username }}
        </p>

        <q-space />

        <q-separator dark vertical />
        <q-btn stretch flat label="Login" to="/login" />
        <q-separator dark vertical />
        <q-btn stretch flat label="Sign up" to="/register" />
        <q-separator dark vertical />
        <q-btn
          v-if="userLogged == true"
          stretch
          flat
          label="Logout"
          to="/logout"
        />
        <q-separator v-if="userLogged == true" dark vertical />
        <q-btn stretch flat label="About" to="/about" />
        <q-separator v-if="userLogged == true" dark vertical />
        <q-btn
          v-if="userLogged == true"
          stretch
          flat
          label="Conversations"
          to="/conversations"
        />
      </q-toolbar>
    </div>
  </header>

  <RouterView />
</template>
