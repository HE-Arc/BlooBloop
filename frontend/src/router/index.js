import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import axios from "axios";

import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();

const API_URL = import.meta.env.VITE_API_URL;

const isUserAuthentificated = async () => {
  const csrfToken = cookies.get("csrftoken");

  const res = await axios.get(API_URL + "profile-items/authenticated/", {
    headers: {
      "x-csrftoken": csrfToken,
      accept: "application/json",
      "content-type": "application/json",
    },
    withCredentials: true,
  });

  console.log(res.data);

  return res.data;
};

const logout = async () => {
  const csrfToken = cookies.get("csrftoken");

  await axios.post(API_URL + "profile-items/logout/", {
    headers: {
      "x-csrftoken": csrfToken,
      accept: "application/json",
      "content-type": "application/json",
    },
    withCredentials: true,
  });
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      async beforeEnter() {
        if (!(await isUserAuthentificated())) {
          return { name: "login" };
        }
      },
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/register",
      name: "register",
      component: () => import("../views/Register.vue"),
    },
    {
      path: "/login",
      name: "login",

      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/logout",
      name: "logout",
      component: () => import("../views/LoginView.vue"),
      beforeEnter() {
        logout();
      },
    },
    {
      path: "/conversations",
      name: "conversations.index",
      component: () => import("../views/Conversations-index.vue"),
      async beforeEnter() {
        if (!(await isUserAuthentificated())) {
          return { name: "login" };
        }
      },
    },
    {
      path: "/conversations/create",
      name: "conversations.create",
      component: () => import("../views/Conversations-create.vue"),
      async beforeEnter() {
        if (!(await isUserAuthentificated())) {
          return { name: "login" };
        }
      },
    },
  ],
});

export default router;
