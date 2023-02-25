<template></template>
<script>
export default {
    middleware: 'auth',
    async created() {
        this.$auth.strategy.token.reset()
        await this.$auth.logout();
    },
}
</script>