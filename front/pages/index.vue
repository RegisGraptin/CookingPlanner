<template>

  <div>

    <HomeBackground />
    
    <HomeFeatures />

    <HomeContact />
    
  </div>

</template>

<script>
import HomeBackground from '~/components/home/HomeBackground.vue';
import HomeFeatures from '~/components/home/HomeFeatures.vue';
import HomeContact from '~/components/home/HomeContact.vue';

export default {
  name: 'IndexPage',
  components: { HomeBackground, HomeFeatures, HomeContact },
}
</script>
