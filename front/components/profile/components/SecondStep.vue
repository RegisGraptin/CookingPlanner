<template>
    <section>

        <div v-for="item in items">
            <ChooseWidget :key_name="item.key" :title="item.title" :variable="profile" :items="item.value" @updateValue="updateValue" />
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
                    profile_variable: this.profile,
                    title: "Spicy level",
                    value: [
                        { name: "Not Spicy", value: 0, icon: "profile/spicy/none.png" },
                        { name: "Soft", value: 1, icon: "profile/spicy/normal.png" },
                        { name: "Spicy", value: 2, icon: "profile/spicy/spicy.png" },
                    ],
                },
                {
                    key: "culinary_adventurousness",
                    profile_variable: this.profile,
                    title: "Culinary Adventurousness",
                    value: [
                        { name: "Not Adventurious", value: 0, icon: "profile/adventurousness/not.png" },
                        { name: "Normal", value: 1, icon: "profile/adventurousness/normal.png" },
                        { name: "Adventurious", value: 2, icon: "profile/adventurousness/adventurious.png" },
                    ],
                },
                {
                    key: "recipe_diversity",
                    profile_variable: this.profile,
                    title: "Recipe diversity",
                    value: [
                        { name: "2/3 recipes", value: 0, icon: "profile/recipe_diversity/low.png" },
                        { name: "3/4 recipes", value: 4, icon: "profile/recipe_diversity/medium.png" },
                        { name: "5+ recipes", value: 7, icon: "profile/recipe_diversity/high.png" },
                    ],
                },
                {
                    key: "ingredient_diversity",
                    profile_variable: this.profile,
                    title: "Ingredient diversity",
                    value: [
                        { name: "few ingredients", value: 0, icon: "profile/ingredient_diversity/few.png" },
                        { name: "Normal", value: 1, icon: "profile/ingredient_diversity/normal.png" },
                        { name: "Large amount", value: 2, icon: "profile/ingredient_diversity/large.png" },
                    ],
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
