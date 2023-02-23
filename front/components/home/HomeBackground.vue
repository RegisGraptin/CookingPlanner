<template>

    <div class="presentation_background">
        <div class="container max-height relative">

            <header id="logo">

                <nav class="relative flex flex-row" id="top-menu">

                    <div class="flex content-center" id="menu-nav-links">
                        <h1 id="menu-title font-semibold">Cooking Planner</h1>

                        <div class="flex space-x-4 nav-links">
                            <a href="#" class="font-semibold">Home</a>
                            <a href="#" class="font-semibold">Features</a>
                            <a href="#" class="font-semibold">Contact</a>
                        </div>
                    </div>


                    
                    <div class="absolute flex content-center right-0">


                        <div class="white-button max-w-sm shadow-lg ring-1 ring-black/5 rounded-xl gap-6 dark:highlight-white/5 mr-5 z-10">
                            <div class="py-3 pl-5 pr-5">
                                <NuxtLink to="/auth/login">
                                    <a href="#" class="font-semibold text-gray-900 hover:text-gray-900">
                                        Login
                                    </a>
                                </NuxtLink>
                            </div>
                        </div>

                        <div class="white-button max-w-sm shadow-lg ring-1 ring-black/5 rounded-xl gap-6 dark:highlight-white/5 z-10">
                            <div class="py-3 pl-5 pr-5">
                                <NuxtLink to="/auth/register">
                                    <a href="#" class="font-semibold text-gray-900 hover:text-gray-900">
                                        Sign up
                                    </a>
                                </NuxtLink>
                            </div>
                        </div>


                    </div>

                </nav>



            </header>

            <section class="presentation_content">

                <article>
                    <h1 class="landing-title">
                        Cooking<br />
                        <span class="shift-name">Planner</span>
                    </h1>

                    <p>La nouvelle application qui te permet d'organiser tes repas de la semaine.</p>
                    <p>Envie de varier ?</p>

                    <p>
                        <NuxtLink to="/generate">
                            Essayer maintenant
                        </NuxtLink>
                    </p>
                </article>

                <article class="absolute bottom-0 right-0">
                    <img class="object-right-bottom mr-20" src="@/assets/images/home/mama.svg" alt="Cooking person"
                        width="400px" />
                </article>

            </section>

        </div>
    </div>
</template>

<style>
header {
    padding-top: 10px;
}

#menu-title {
    padding-right: 80px;
    font-size: 20px;
    font-weight: 600;
}

nav#top-menu,
#menu-nav-links {
    align-items: center;
}

.nav-links>a {
    padding-left: 30px;
    color: #333333b3;
}

.nav-links>a:hover {
    color: #333333;
}

.presentation_background {
    height: 500px;
    background-color: #febd2e;


    margin-left: 7px;
    margin-right: 7px;
    margin-top: 7px;

    border-radius: 30px;

    /* min-height: 850px; */
    /* height: 100vh; */

    /* background: url("~assets/images/home/background.jpg") no-repeat center center; */
    /* background-size: cover; */
    /* position: relative; */
}

h1.landing-title {
    font-size: 80px;
    line-height: 80px;
    padding-bottom: 50px;
}

h1.landing-title>.shift-name {
    padding-left: 50px;
}


.presentation_content {
    padding-top: 50px;
}

.max-height {
    height: 100%;
    padding-bottom: 0;
}

.image-bottom-right {
    position: relative;
    height: 100%;
}

.image-bottom-right>img {
    height: auto;
    position: absolute;
    right: 0;
    bottom: 0;
    /* right: 0;
    bottom: 0; */
}

.white-button {
    background-color: white;
    color: #333333;
}
</style>

<script>
export default {}
</script>
