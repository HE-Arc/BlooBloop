import axios from "axios";
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();

export default class AxiosService {
  /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\
  |*                           PRIVATE                           *|
  \* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

  static #HEADER_CONFIG = {
    headers: {
      "x-csrftoken": cookies.get("csrftoken"),
      accept: "application/json",
      "content-type": "application/json",
    },
    withCredentials: true,
  };

  /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\
  |*                           PUBLIC                            *|
  \* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

  static updateCsrfToken() {
    AxiosService.#HEADER_CONFIG.headers['x-csrftoken'] = cookies.get("csrftoken");
  }

  static get GET() {
    return axios.create(AxiosService.#HEADER_CONFIG).get;
  }

  static get POST() {
    return axios.create(AxiosService.#HEADER_CONFIG).post;
  }

  static get PUT() {
    return axios.create(AxiosService.#HEADER_CONFIG).put;
  }

  static get PATCH() {
    return axios.create(AxiosService.#HEADER_CONFIG).patch;
  }

  static get DELETE() {
    return axios.create(AxiosService.#HEADER_CONFIG).delete;
  }
}
