<template>
  <v-app>
    
    <v-main>
        <Nuxt />
    </v-main>
    
    <v-footer>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {}
  }
}
</script>

<style scoped>

main {
  background-color: #f5f3f0;
  color: #333333;
}

html {
    scroll-behavior: smooth;
}

</style>
