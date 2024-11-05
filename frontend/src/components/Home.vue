<template>
  <div>
    <h1>Select Your Psychologist</h1>
    <button @click="selectPsychologist(1)">Sigmund Freud</button>
    <button @click="selectPsychologist(2)">Carl Jung</button>
    <button @click="selectPsychologist(3)">Alfred Adler</button>
  </div>
</template>

<script>
export default {
  methods: {
    selectPsychologist(id) {
      // Navigate to the introduction page for the selected psychologist
      this.$router.push(`/psychologist/${id}/intro`);
    }
  }
};
</script>
