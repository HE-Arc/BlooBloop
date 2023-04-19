<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute, useRouter, RouterView } from "vue-router";
import AxiosService from "../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;

const route = useRoute();
const router = useRouter();

const userLogged = ref(false);
const username = ref("");

const logout = async () => {
  await AxiosService.POST(`${API_URL}profile-items/logout/`).then(() => {
    userLogged.value = false;
    username.value = "";
    localStorage.removeItem("user");
    router.push({ path: "/" });
  });
};

const updateUser = () => {
  let user = localStorage.getItem("user");

  if (user != null) {
    userLogged.value = true;
    username.value = user.toUpperCase();
  } else {
    userLogged.value = false;
    username.value = "";
  }
};

watch(
  () => route.path,
  async () => {
    updateUser();
  }
);

onMounted(async () => {
  updateUser();
});
</script>

<template>
  <header>
    <div class="q-pa-md">
      <q-toolbar class="bg-primary text-white q-my-md shadow-2">
        <q-btn stretch flat label="BlooBloop" to="/" />

        <q-space />

        <p v-if="userLogged" class="text-h6" style="margin: 0px">
          {{ username }}
        </p>

        <q-space />

        <q-separator dark vertical v-if="!userLogged" />
        <q-btn stretch flat label="Login" to="/login" v-if="!userLogged" />
        <q-separator dark vertical v-if="!userLogged" />
        <q-btn stretch flat label="Sign up" to="/register" v-if="!userLogged" />
        <q-separator v-if="userLogged" dark vertical />
        <q-btn v-if="userLogged" stretch flat label="Logout" @click="logout" />
        <q-separator dark vertical />
        <q-btn stretch flat label="About" to="/about" />
        <q-separator v-if="userLogged" dark vertical />
        <q-btn
          v-if="userLogged"
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
