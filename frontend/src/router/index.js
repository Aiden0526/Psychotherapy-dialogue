import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';          // Import HomePage
import PsychologistIntro from '@/components/PsychologistIntro.vue';  // Import PsychologistIntro
import PsychologistChat from '@/components/PsychologistChat.vue'; // Import PsychologistChat

const routes = [
  {
    path: '/',           // Home route
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/psychologist/:id/intro',  // Route for psychologist introduction page
    name: 'PsychologistIntro',
    component: PsychologistIntro
  },
  {
    path: '/psychologist/:id/chat',
    name: 'PsychologistChat', // Route for psychologist chat page
    component: PsychologistChat
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
