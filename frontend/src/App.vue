<template>
  <div id="app">
    <FilterBadWords/>
  </div>
</template>

<script>
import FilterBadWords from './components/FilterBadWords.vue'

export default {
  name: 'App',
  components: {
    FilterBadWords
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
