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
    /**
     * Handles psychologist selection by navigating to the introduction page
     * @param {Number} id - The ID of the selected psychologist (1: Freud, 2: Jung, 3: Adler)
     */
    selectPsychologist(id) {
      // Navigate to the introduction page for the selected psychologist
      this.$router.push(`/psychologist/${id}/intro`);
    }
  }
};
</script>
