<script setup>
import axios from "axios";
import { ref } from "vue";

const username = ref("");
const email = ref("");
const password = ref("");
const isPwd = ref(true);

const success = ref(false);
const errors = ref(null);

const isValidEmail = (val) => {
  const emailPattern =
    /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;
  return emailPattern.test(val) || "Invalid email";
};

const submit = async () => {
  try {
    success.value = false;
    errors.value = null;

    await axios.post("http://127.0.0.1:8000/api/profile-items/", {
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

  <div class="q-pa-md" style="max-width: 50%">
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

      <div class="row q-mt-lg justify-around">
        <q-btn label="Sign up" type="submit" color="primary" />
        <a href="/users/login">Log in</a>
      </div>
    </q-form>
  </div>
</template>
