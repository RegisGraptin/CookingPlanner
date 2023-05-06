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
    props: {
        profile: Object
    },
    created() {
        console.log(this.$route.params);
        console.log(this.$route.params.profile);
        console.log(this.profile);
        console.log(this.generated_week);
    }
}
</script>
 