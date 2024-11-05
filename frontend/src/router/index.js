import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';          // Import HomePage
import PsychologistIntro from '@/components/PsychologistIntro.vue';  // Import PsychologistIntro

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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
