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

            api.generateWeekUnique(this.$axios).then((week) => {
                this.generateWeek = week;
                this.$log.debug(this.generated_week);
            }).catch((err) => {
                // Set the log for the error
                this.$log.error("Can't fetch the generated week");
                this.$log.error(err);

                // Show a alert for the user
                this.$toast.show({
                    type: 'warning',
                    title: 'Error',
                    message: 'Internal error! Can\'t generate a new week.',
                    classToast: ""
                })

            })


//             <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
//   <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z" />
// </svg>


            
        }
    },
    components: { DisplayWeek }
}
</script>
