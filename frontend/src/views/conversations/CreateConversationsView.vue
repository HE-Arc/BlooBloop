<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import AxiosService from "../../../utils/AxiosService.mjs";

// Environment variable setup
const API_URL = import.meta.env.VITE_API_URL;
const router = useRouter();
const errors = ref(null);

// Conversation variable setup
const name = ref("");
const selectedUsers = ref([]);
const profileOptions = [];

// Create a conversation
const submit = async () => {
  try {
    errors.value = null;

    let profiles = [];
    selectedUsers.value.forEach((user) => profiles.push(user.id));

    await AxiosService.POST(`${API_URL}conversation-items/custom-post/`, {
      name: name.value,
      users: profiles,
    }).then(() => {
      router.push({
        path: "/conversations",
      });
    });
  } catch (error) {
    errors.value = error.response.data.error;
  }
};

// Retrieve users
const fetchUserItems = async () => {
  await AxiosService.GET(`${API_URL}profile-items/`).then((response) => {
    selectedUsers.value = [response.data[0]];
    response.data.forEach((profile) => {
      profileOptions.push({ label: profile.user.username, value: profile });
    });
  });
};

onMounted(() => {
  fetchUserItems();
});
</script>

<template>
  <div class="q-mx-lg">
    <q-banner v-if="errors" dense inline-actions class="text-white bg-red">
      {{ errors }}
    </q-banner>
  </div>

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

        <p class="text-weight-bold">Users</p>
        <q-option-group
          v-model="selectedUsers"
          :options="profileOptions"
          color="green"
          type="checkbox"
        />
        <div class="row justify-center">
          <q-btn label="Create" type="submit" color="primary" />
        </div>
      </q-form>
    </div>
  </main>
</template>
