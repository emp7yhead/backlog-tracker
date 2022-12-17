import { createApp } from 'vue';
import './style.css';
import axios from 'axios';

import router from './router/index.js'
import App from './App.vue';


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';

createApp(App)
.use(router)
.mount('#app')
