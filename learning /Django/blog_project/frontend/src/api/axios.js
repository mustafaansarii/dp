import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/', // Change it to your backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor to include JWT token in requests
axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem('access'); // Retrieve token from local storage
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
});

export default axiosInstance;
