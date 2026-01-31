import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const uploadVideo = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return API.post("/upload", formData);
};

export const processVideo = (jobId) => {
  return API.post(`/process/${jobId}`);
};

export const downloadVideoUrl = (jobId) => {
  return `http://127.0.0.1:8000/download/${jobId}/video`;
};
