import axios from "axios";

const API = axios.create({
  baseURL: "https://your-backend.onrender.com"
});

export const createTransaction = (data) =>
  API.post("/transaction", data);

export const getSummary = (userId) =>
  API.get(`/summary/${userId}`);

export const getRanking = () =>
  API.get("/ranking");