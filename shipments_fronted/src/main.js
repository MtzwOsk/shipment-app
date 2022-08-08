import 'vuetify/styles'; // Global CSS has to be imported
import '@mdi/font/css/materialdesignicons.css';
import {createApp} from 'vue';
import App from './App.vue';
import router from './router';
import Notifications from '@kyvg/vue3-notification';
import {createVuetify} from 'vuetify';


const app = createApp(App);
const vuetify = createVuetify({
    theme: {
        defaultTheme: 'dark'
    },
    icons: {
        iconfont: 'mdi',
    },
});

app.use(vuetify);
app.use(router);
app.use(Notifications);

app.mount('#app');
