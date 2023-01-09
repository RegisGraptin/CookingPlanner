<template>

    <v-container tag="section" lg>

            <h2>Week generated</h2>

            <p>blabla</p>
            
            <v-btn large @click="generateWeek">
                Generate data
            </v-btn>


    </v-container>

</template>

<script>

import { CookingPlannerAPI } from '~/api/cooking_planner';

export default {
    name: 'Generate',
    data() {
        return {
            generated_week: null
        }
    },
    methods: {
        async generateWeek() {
            let api = new CookingPlannerAPI();
            this.generated_week = await api.generateWeekUnique(this.$axios);
        }
    }
}
</script>
