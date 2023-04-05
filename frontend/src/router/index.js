import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

const isUserAuthentificated = async () => {
  const res = await axios.get(API_URL + "profile-items/authenticated/");
  console.log(res.data);
  // TODO : Fixme
  return true;
};

const logout = async () => {
  await axios.post(API_URL + "profile-items/logout/");
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      beforeEnter() {
        if (!isUserAuthentificated()) {
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
      component: () => import("../views/CreateUserView.vue"),
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
      beforeEnter() {
        if (!isUserAuthentificated()) {
          return { name: "login" };
        }
      },
    },
    {
      path: "/conversations/create",
      name: "conversations.create",
      component: () => import("../views/Conversations-create.vue"),
      beforeEnter() {
        if (!isUserAuthentificated()) {
          return { name: "login" };
        }
      },
    },
  ],
});

export default router;
