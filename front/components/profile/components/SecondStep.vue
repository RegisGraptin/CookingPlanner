<template>
   <section>
        
        <div v-for="item in items">
            <h2>{{ item.key }}</h2>
            <ChooseWidget :key_name="item.key" :variable="profile" :items="item.value" @updateValue="updateValue" />
        </div>


    </section>
</template>
<script>

// seasonal_recipe: true,          // true or false
// spicy: 3,                       // spicy level
// culinary_adventurousness: 3,    // [0:5]
// recipe_diversity: 4,            // [0:7]
// ingredient_diversity: 3,        // [0:5]

import ChooseWidget from '../widgets/ChooseWidget.vue';


export default {
    name: "",
    props: {
        profile: Object
    },
    data() {
        return {

            items: [
                // {
                //     key: "seasonal_recipe",
                //     value: [
                //         {name: "False", value: true, icon: ""},    
                //         {name: "True", value: false, icon: ""},
                //     ],
                //     profile_variable: this.profile.seasonal_recipe,
                // },
                {
                    key: "spicy",
                    value: [
                        {name: "Not Spicy", value: 0, icon: ""},
                        {name: "Soft", value: 1, icon: ""},
                        {name: "Spicy", value: 2, icon: ""},  
                    ],
                    profile_variable: this.profile,
                },
                {
                    key: "culinary_adventurousness",
                    value: [
                        {name: "Not Adventurious", value: 0, icon: ""},
                        {name: "Normal", value: 1, icon: ""},
                        {name: "Adventurious", value: 2, icon: ""},
                    ],
                    profile_variable: this.profile,
                },
                {
                    key: "recipe_diversity",
                    value: [
                        {name: "2/3 recipes", value: 0, icon: ""},
                        {name: "3/4 recipes", value: 4, icon: ""},
                        {name: "5+ recipes", value: 7, icon: ""},
                    ],
                    profile_variable: this.profile,
                },
                {
                    key: "ingredient_diversity",
                    value: [
                        {name: "few ingredients", value: 0, icon: ""},
                        {name: "Normal", value: 1, icon: ""},
                        {name: "Large amount", value: 2, icon: ""},
                    ],
                    profile_variable: this.profile,
                },

            ],            
        }
    },
    methods: {
        updateValue(key, value) {
            this.profile[key] = value;
        }
    },
    components: { ChooseWidget }
}
</script>
