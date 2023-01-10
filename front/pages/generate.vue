<template>

    <v-container tag="section" lg>

            <h2>Week generated</h2>

            <p>blabla</p>
            
            <v-btn large @click="generateWeek">
                Generate data
            </v-btn>

            <v-container v-if="generated_week">
                <h2>Generted Week</h2>
                
                <DisplayWeek :week="generated_week"></DisplayWeek>

            </v-container>


    </v-container>

</template>

<script>

import { CookingPlannerAPI } from '~/api/cooking_planner';
import DisplayWeek from '~/components/planning/DisplayWeek.vue';

export default {
    name: "Generate",
    data: () => ({
        generated_week: null
    }),
    methods: {
        async generateWeek() {
            this.$log.debug("Generate a new week.");
            let api = new CookingPlannerAPI();
            this.generated_week = await api.generateWeekUnique(this.$axios);
            this.$log.debug(this.generated_week);
        }
    },
    components: { DisplayWeek }
}
</script>
