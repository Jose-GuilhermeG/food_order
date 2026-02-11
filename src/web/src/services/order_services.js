import axios from "axios";


const BASE_WS_URL = "ws://localhost:8000/"
const BASE_URL = "http://localhost:8000/"

export const get_preparing_orders = (path = "orders/")=>new WebSocket(BASE_WS_URL + path)
export const get_ready_order = (path = "orders/ready/")=>new WebSocket(BASE_WS_URL + path)

export const register_order = (data , path = "orders/") => axios.post(BASE_URL + path , data)
