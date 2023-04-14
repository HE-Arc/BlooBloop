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

  static get GET() {
    return axios.create(AxiosService.#HEADER_CONFIG).get;
  }

  static get POST() {
    return axios.create(AxiosService.#HEADER_CONFIG).post;
  }

  static get DELETE() {
    return axios.create(AxiosService.#HEADER_CONFIG).delete;
  }
}
