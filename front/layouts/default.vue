<template>
  <app>
    
    <main>
        <Nuxt />
    </main>
    
    <Footer />
  </app>
</template>

<script>

import Footer from '../components/page/Footer.vue';

export default {
  name: 'DefaultLayout',
  components: {
    Footer,
  },
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
