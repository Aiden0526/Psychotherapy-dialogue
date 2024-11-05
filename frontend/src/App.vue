<template>
  <div id="app">
    <HomePage />
  </div>
</template>

<script>
import HomePage from './components/HomePage.vue'  // Import the renamed component

export default {
  name: 'App',
  components: {
    HomePage  // Register the component
  }
}
</script>