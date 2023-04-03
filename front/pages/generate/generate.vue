<template></template>
<script>

export default {
    name: "",
    middleware: 'auth',
    data() {
        return {
            profile: null,
            generated_week: null,
        }
    },
    mounted() {
        console.log(this.$route.params);
    }
}
</script>
 