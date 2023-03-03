<template>
  <app class="flex flex-col h-screen justify-between">
    
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

html {
  scroll-behavior: smooth;
  background-color: #f5f3f0;
  color: #333333;
}

</style>
