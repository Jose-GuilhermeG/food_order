import axios from "axios";

const BASE_URL = "http://localhost:8000/"

export const get_all_food = async (path = "food/") => axios.get(BASE_URL + path)

export const get_food_by_category = async (slug , path = "category/") => axios.get(BASE_URL + path + slug + "/")

export const get_food_details = async (food_slug , path = "food/") => axios.get(BASE_URL + path + food_slug + "/")
