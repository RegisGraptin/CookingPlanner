<template>
    <main>

        <section>
            <h2>Week generated</h2>

            <p>blabla</p>
            
            <v-btn large @click="generateWeek">
                Generate data
            </v-btn>


        </section>

    </main>
</template>

<script>

import { CookingPlannerAPI } from '~/api/cooking_planner';

export default {
    name: 'Generate',
    methods: {
        async generateWeek() {
            console.log("Generate a new week process")

            let api = new CookingPlannerAPI();
            let generated_week = await api.generateWeekUnique(this.$axios);
            console.log("Generated week")
            console.log(generated_week)
        }
    }
}
</script>
