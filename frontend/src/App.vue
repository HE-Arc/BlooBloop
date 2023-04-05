<script setup>
import { RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="q-pa-md">
      <q-toolbar class="bg-primary text-white q-my-md shadow-2">
        <q-btn stretch flat label="BlooBloop" to="/" />

        <q-space />

        <q-separator dark vertical />
        <q-btn stretch flat label="Login" to="/login" />
        <q-separator dark vertical />
        <q-btn stretch flat label="Sign up" to="/register" />
        <q-separator dark vertical />
        <q-btn stretch flat label="Logout" to="/logout" />
        <q-separator dark vertical />
        <q-btn stretch flat label="About" to="/about" />
        <q-separator dark vertical />
        <q-btn stretch flat label="Conversations" to="/conversations" />
      </q-toolbar>
    </div>
  </header>

  <RouterView />
</template>
