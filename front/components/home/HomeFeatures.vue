<template>
    <section class="question-features container grid grid-cols-2">

        <article class="grid grid grid-cols-2">

            <img src="@/assets/images/home/question_girl.svg" />

            <article>

                <div class="question-card max-w-sm mx-auto shadow-lg ring-1 ring-black/5 rounded-xl flex items-center gap-6 dark:highlight-white/5">
                    <div class="py-5 pl-5">
                        <strong class="text-slate-900 text-sm font-medium">Idée de recette simple et rapide pour le soir ?</strong>
                    </div>
                </div>
                <div class="question-card max-w-sm mx-auto shadow-lg ring-1 ring-black/5 rounded-xl flex items-center gap-6 dark:highlight-white/5">
                    <div class="py-5 pl-5">
                        <strong class="text-slate-900 text-sm font-medium">Quel recette de cuisine pour la semaine ?</strong>
                    </div>
                </div>
                <div class="question-card max-w-sm mx-auto shadow-lg ring-1 ring-black/5 rounded-xl flex items-center gap-6 dark:highlight-white/5">
                    <div class="py-5 pl-5">
                        <strong class="text-slate-900 text-sm font-medium">Comment préparer ses repas pour la semaine ?</strong>
                    </div>
                </div>

            </article>

        </article>

        <article>

            <div class="question-card-answer max-w-sm shadow-lg ring-1 ring-black/5 rounded-xl flex items-center gap-6 dark:highlight-white/5">
                <div class="py-5 pl-5 pr-5">
                    <p>
                        En manque d'inspiration ou pas d'idée ?
                        
                        Cooking Planner est l'outil qui vous simplifie la vie. En fonction de vos préférences et de vos repas, Cooking Planner génère des recettes 
                        de cuisines pour chacun des plats de la semaines. Il ne vous reste plus qu'à réaliser vos courses et à prendre le temps de cuisiner.


                    </p>
                </div>
            </div>
        </article>

    </section>
</template>

<style scoped>

.question-features {
    padding-top: 50px;
}

.question-card {
    background-color: #febd2e;
    color: #333333;
    margin-bottom: 10px;
}

.question-card-answer {
    background-color: #febd2e;
    color: #333333;
    text-align: justify;
    margin-left: 50px;
}



</style>