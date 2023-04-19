<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import AxiosService from "../../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;
const route = useRoute();
const router = useRouter();

const name = ref("");

const fetchConversation = async () => {
  await AxiosService.GET(
    `${API_URL}conversation-items/${route.params.id}/`
  ).then((response) => {
    name.value = response.data.name;
  });
};
const submit = async () => {
  await AxiosService.PATCH(`${API_URL}conversation-items/${route.params.id}/`, {
    name: name.value,
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
