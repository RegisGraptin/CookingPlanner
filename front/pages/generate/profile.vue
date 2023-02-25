<template>
    <section>

        <h2>Create a new profile</h2>

        <ul>
            <li>Profile 1</li>
            <li>Profile 2</li>
        </ul>

        <button v-on:click="getProfiles">Get profiles</button>

    </section>
</template>
<script>

import { CookingPlannerAPI } from '~/api/cooking_planner';

export default {
    middleware: 'auth',
    methods: {
        async getProfiles() {

            let api = new CookingPlannerAPI();
            await api.getProfiles(this.$axios);

        }
    }
}
</script>