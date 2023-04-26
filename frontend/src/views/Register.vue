<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";
import AxiosService from "../../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;
const router = useRouter();

const username = ref("");
const email = ref("");
const password = ref("");
const isPwd = ref(true);

const errors = ref(null);

const isValidEmail = (val) => {
  const emailPattern =
    /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;
  return emailPattern.test(val) || "Invalid email";
};

const submit = async () => {
  errors.value = null;

  await AxiosService.POST(`${API_URL}profile-items/register/`, {
    username: username.value,
    email: email.value,
    password: password.value,
  })
    .then(async () => {
      await AxiosService.POST(`${API_URL}profile-items/login/`, {
        username: username.value,
        password: password.value,
      }).then(() => {
        AxiosService.updateCsrfToken();
        localStorage.setItem("user", username.value);
        router.push({
          path: "/",
        });
      });
    })
    .catch((error) => {
      errors.value = error.response.data.error;
    });
};
</script>

<template>
  <div class="q-mx-lg">
    <q-banner v-if="errors" dense inline-actions class="text-white bg-red">
      {{ errors }}
    </q-banner>
  </div>

  <main>
    <div class="q-mx-auto q-mt-xl" style="max-width: 50%">
      <h3>Sign up</h3>
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
          square
          filled
          type="email"
          v-model="email"
          label="Email"
          :rules="[(val) => !!val || 'Email is missing', isValidEmail]"
        />

        <q-input
          v-model="password"
          square
          filled
          label="Password"
          :type="isPwd ? 'password' : 'text'"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || 'Password is missing']"
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
          <q-btn label="Sign up" type="submit" color="primary" />
          <router-link to="/login">Log in</router-link>
        </div>
      </q-form>
    </div>
  </main>
</template>
