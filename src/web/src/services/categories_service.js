import axios from "axios";

const BASE_URL = "http://localhost:8000/"

export const get_all_categories = async (path = "category/") => axios.get(BASE_URL + path)
