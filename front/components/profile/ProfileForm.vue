<template>

    <section class="container mx-auto min-h-screen">

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
        

        <article class="flex justify-evenly mt-5 mb-5">

            <button @click="previousStep" :disabled="current_step===0" class="inline-flex items-center justify-between w-32 p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 disabled:opacity-25">Previous</button>

            <button @click="nextStep" :disabled="current_step===totalSteps()-1" class="inline-flex items-center justify-between w-32 p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 disabled:opacity-25">Next</button>
        </article>
    </section>

</template>
<script>

import FirstStep from './components/FirstStep.vue';
import SecondStep from './components/SecondStep.vue';
import ThirdStep from './components/ThirdStep.vue';

export default {
    name: "ProfileForm",
    data() {
        return {
            current_step: 0,
            steps: [
                FirstStep,
                SecondStep,
                ThirdStep,
            ],


            create_profile: {
                n_persons: 2,                   // [1:10]
                cost: 3,                        // [0:5]
                
                cooking_level: 3,               // [0:5]
                cooking_time: 3,                // [0:5]

                seasonal_recipe: true,          // true or false
                spicy: 1,                       // spicy level
                culinary_adventurousness: 1,    // [0:5]
                recipe_diversity: 4,            // [0:7]
                ingredient_diversity: 1,        // [0:5]
                
                
            }




        }
    },
    methods: {
        nextStep() {
            if (this.current_step < this.totalSteps() - 1) {
                this.current_step++;
            }
        },
        previousStep() {
            if (this.current_step > 0) {
                this.current_step--;
            }
        },
        totalSteps() {
            return this.steps.length;
        }
    }
}
</script>
