<template>
    <v-container class="scroll-smooth">

        <section class="calendar w-full flex gap-6 snap-mandatory snap-x overflow-x-auto pb-14">


            <article class="calendar-day snap-center shrink-0 first:pl-8 last:pr-8" v-for="day in week.days" :key="day.date">
                

                    <div>
                        <h3 class="text-center">{{ getDateInformation(day.date) }}</h3>
                    </div>

                    <div class="font-weight-bold" v-for="meal in day.meals.sort((a, b) => a.moment - b.moment)" :key="meal">

                        <div class="title">
                            <v-card-title>
                                <span>{{ meal.dish.name }}</span>
                            </v-card-title>
                            <v-card-text>
                                <p>Moment: {{ meal.moment }}</p>
                                <p>Duration: {{ meal.dish.duration }}</p>
                                <a href="#">Recette</a>
                            </v-card-text>
                            
                        </div>

                    </div>

            </article>



            

        </section>

    </v-container>
</template>

<style scoped>
section.calendar {
    /* display: flex;
    flex-wrap: wrap;
    justify-content: space-around; */
}

article.calendar-day {
    width: 250px;
    height: 700px;
    margin-right: 10px;
}

h3.text-center {
    width: 100%;
    text-align: center;
}

</style>

<script>

export default {
    name: "DisplayWeek",
    props: {
        week: Object
    },
    methods: {
        getDateInformation(date) {
            /**
             * Get a date with YYYY-MM-DD format.
             * Change it to name of the day - Day number 
             */

            let date_information = date.split('-')

            return this.getNameWeekDay(date) + " - " + date_information[2]
        },
        getNameWeekDay(date) {
            const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

            const d = new Date(date);

            return weekday[d.getDay()];
        }
    }
}
</script>
