<template>
   <section>
        <div v-for="item in items">
            <ChooseWidget :key_name="item.key" :title="item.title" :variable="profile" :items="item.value" />
        </div>
    </section>
</template>
<script>

import ChooseWidget from '../widgets/ChooseWidget.vue';

export default {
    name: "ThirdStepProfileCreation",
    components: { ChooseWidget },
    props: {
        profile: Object
    },
    data(){
        // https://www.flaticon.com/free-icon/calendar_3143636?term=calendar&page=1&position=22&origin=search&related_id=3143636
        return {
            items: [
                {
                    key: "seasonal_recipe",
                    profile_variable: this.profile,
                    title: "Seasonal Recipe",
                    value: [
                        {name: "Non Seasonal Recipe", value: false, icon: "profile/seasonal_recipe/season.png"},
                        {name: "Seasonal Recipe", value: true, icon: "profile/seasonal_recipe/season.png"},
                    ],
                },
            ]
        }
    }
}
</script>
