<template>
  <NavBar />
  <div id="app">
    <div class="relative px-6 lg:px-8">
        <router-view/>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
export default {
  components: {
    NavBar
  }
}
</script>
