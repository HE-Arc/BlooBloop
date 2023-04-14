import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AxiosService from "../../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;

const isUserAuthentificated = async () => {
  const res = await AxiosService.GET(API_URL + "profile-items/authenticated/");
  return res.data;
};

const logout = async () => {
  await AxiosService.POST(API_URL + "profile-items/logout/");
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      props: true,
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
      async beforeEnter() {
        await logout();
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
