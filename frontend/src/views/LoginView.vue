<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import AxiosService from "../../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;
const router = useRouter();

const username = ref("");
const password = ref("");
const isPwd = ref(true);

const errors = ref(null);

const submit = async () => {
  errors.value = null;

  await AxiosService.POST(`${API_URL}profile-items/login/`, {
    username: username.value,
    password: password.value,
  }).then(
    () => {
      AxiosService.updateCsrfToken();
      localStorage.setItem("user", username.value);
      router.push({
        path: "/",
        params: { alert: "Logged in as " + username.value },
      });
    },
    (error) => {
      errors.value = error.response.data;
    }
  );
};
</script>

<template>
  {{ errors }}

  <main>
    <div class="q-mx-auto q-mt-xl" style="max-width: 50%">
      <h3>Login</h3>
      <q-form @submit="submit" class="q-gutter-md">
        <q-input
          square
          filled
          v-model="username"
          label="Username"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Username is missing']"
        />

        <q-input
          v-model="password"
          square
          filled
          label="Password"
          :type="isPwd ? 'password' : 'text'"
          lazy-rules
          :rules="[
            (val) => (val && val.length >= 8) || 'Password is too short',
          ]"
        >
          <template v-slot:append>
            <q-icon
              :name="isPwd ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwd = !isPwd"
            />
          </template>
        </q-input>

        <div class="row q-mt-lg justify-around items-center">
          <q-btn label="Login" type="submit" color="primary" />
          <router-link to="/register">Sign up</router-link>
        </div>
      </q-form>
    </div>
  </main>
</template>
