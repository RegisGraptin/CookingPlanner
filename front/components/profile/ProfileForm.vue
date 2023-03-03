<template>

    <section class="container mx-auto">

        <section class="p-10">
            <div class="flex items-stretch gap-2">
                <div
                v-for="step in totalSteps()"
                class="h-2 w-full rounded text-purple-500"
                style="border: 1px solid;"
                :class="{'bg-purple-500 ': step - 1 <= current_step}"
                ></div>
            </div>
        </section>
        

        <component v-bind:is="steps[current_step]" :profile="create_profile"></component>
        

        <button @click="previousStep">Previous</button>
        <button @click="nextStep">Next</button>
        
    </section>

</template>
<script>

import FirstStep from './components/FirstStep.vue';
import SecondStep from './components/SecondStep.vue';

export default {
    name: "ProfileForm",
    data() {
        return {
            current_step: 0,
            steps: [
                FirstStep,
                SecondStep,
            ],


            create_profile: {
                n_persons: 2,                   // [1:10]
                cost: 3,                        // [0:5]
                
                cooking_level: 3,               // [0:5]
                cooking_time: 3,                // [0:5]

                seasonal_recipe: true,          // true or false
                spicy: 3,                       // spicy level
                culinary_adventurousness: 3,    // [0:5]
                recipe_diversity: 4,            // [0:7]
                ingredient_diversity: 3,        // [0:5]
                
                
            }




        }
    },
    methods: {
        nextStep() {
            this.current_step++;
        },
        previousStep() {
            this.current_step--;
        },
        totalSteps() {
            return this.steps.length;
        }
    }
}
</script>
