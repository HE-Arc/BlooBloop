import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AxiosService from "../../utils/AxiosService.mjs";

const API_URL = import.meta.env.VITE_API_URL;

const authenticationGuard = (to, from, next) => {
  AxiosService.GET(`${API_URL}profile-items/authenticated/`).then(
    (response) => {
      if (response.data) {
        next();
      } else {
        next({ path: "/login" });
      }
    },
    () => {
      next({ path: "/login" });
    }
  );
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
      component: () => import("../views/RegisterView.vue"),
    },
    {
      path: "/login",
      name: "login",

      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/conversations",
      name: "conversations.index",
      component: () => import("../views/conversations/ConversationsView.vue"),
      beforeEnter: authenticationGuard,
    },
    {
      path: "/conversations/create",
      name: "conversations.create",
      component: () =>
        import("../views/conversations/CreateConversationsView.vue"),
      beforeEnter: authenticationGuard,
    },
    {
      path: "/conversations/:id",
      component: () =>
        import("../views/conversations/UpdateConversationsView.vue"),
      beforeEnter: authenticationGuard,
    },
  ],
});

export default router;
