<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import AxiosService from "../../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;
const route = useRoute();
const router = useRouter();

const name = ref("");
const selectedProfiles = ref([]);
const allProfiles = ref([]);

const fetchConversation = async () => {
  await AxiosService.GET(
    `${API_URL}conversation-items/${route.params.id}/`
  ).then((response) => {
    name.value = response.data.name;
    response.data.users.forEach((profile) => {
      selectedProfiles.value.push(profile.id);
    });
  });
};
const fetchProfiles = async () => {
  await AxiosService.GET(`${API_URL}profile-items/`).then((response) => {
    response.data.forEach((profile) => {
      allProfiles.value.push({ label: profile.user.username, value: profile });
    });

    let profiles = selectedProfiles.value;
    selectedProfiles.value = [];
    response.data.forEach((profile) => {
      profiles.forEach((id) => {
        if (profile.id === id) {
          selectedProfiles.value.push(profile);
        }
      });
    });
  });
};

const submit = async () => {
  await AxiosService.PATCH(`${API_URL}conversation-items/${route.params.id}/`, {
    id: route.params.id,
    name: name.value,
    users: selectedProfiles.value,
  }).then(
    () => {
      router.push("/conversations");
    },
    () => {
      router.push("/login");
    }
  );
};

onMounted(async () => {
  await fetchConversation();
  await fetchProfiles();
});
</script>

<template>
  <div class="q-mx-auto">
    <h3>Update Conversation</h3>
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
        v-model="selectedProfiles"
        :options="allProfiles"
        color="green"
        type="checkbox"
      />
      <div class="row justify-center">
        <q-btn label="Update" type="submit" color="primary" />
      </div>
    </q-form>
  </div>
</template>

<style scoped>
.q-mx-auto {
  max-width: 50%;
}
</style>
