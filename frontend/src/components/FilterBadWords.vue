<template>
  <div class="wrapper">
    <div>
      <label>
      Input phrase:
      <textarea v-model="rawText" name="rawText" cols="30" rows="10"></textarea>
    </label>
    </div>

    <button @click="filterPhrase">Filter</button>
    <span class="error" v-if="errorText">{{ errorText }}</span>
    <div>
      <label>
      Output phrase:
      <textarea readonly :value="filteredText" cols="30" rows="10"></textarea>
    </label>
    </div>

  </div>
</template>

<script>
import { filterBadWords } from '@/services/filterBadWords';

export default {
  name: 'FilterBadWords',
  data() {
    return {
      rawText: '',
      filteredText: '',
      errorText: '',
    }
  },
  methods: {
    filterPhrase() {
      filterBadWords(this.rawText)
      .then(filteredData => {
        this.filteredText = filteredData.filteredText
        if (filteredData.errorText) {
          this.errorText = filteredData.errorText
        }
    })
      .catch(error => {
        this.filteredText = ''
        this.errorText = error.message || 'Something went wrong.'
      })
    },
  },
  watch: {
    rawText() {
      this.errorText = '';
    },
  },
}
</script>

<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}
button {
  display: inline-block;
  width: 150px;
  margin: 20px 0;
}
.error {
  color: red;
}
</style>
