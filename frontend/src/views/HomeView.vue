<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const alert = ref("");

onMounted(() => {
  if (router.params) {
    alert.value = router.params.alert;
  }
});
</script>

<template>
  <main>
    <p>{{ alert }}</p>
    <div class="text-center">
      <h3>Ici, pas de <b>bla bla</b> que du <b>bloo bloop !</b></h3>
    </div>
  </main>
</template>
