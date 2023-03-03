<template>
    <div class="presentation-background">
        <div class="presentation-content-layer container mx-auto max-height relative">

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

                        <div v-if="!this.$auth.loggedIn"
                            class="white-button max-w-sm shadow-lg ring-1 ring-black/5 rounded-xl gap-6 dark:highlight-white/5 mr-5 z-10">
                            <div class="py-3 pl-5 pr-5">
                                <NuxtLink to="/auth/login">
                                    <a href="#" class="font-semibold text-gray-900 hover:text-gray-900">
                                        Login
                                    </a>
                                </NuxtLink>
                            </div>
                        </div>

                        <div v-if="!this.$auth.loggedIn"
                            class="white-button max-w-sm shadow-lg ring-1 ring-black/5 rounded-xl gap-6 dark:highlight-white/5 z-10">
                            <div class="py-3 pl-5 pr-5">
                                <NuxtLink to="/auth/register">
                                    <a href="#" class="font-semibold text-gray-900 hover:text-gray-900">
                                        Sign up
                                    </a>
                                </NuxtLink>
                            </div>
                        </div>

                        <div v-if="this.$auth.loggedIn"
                            class="white-button max-w-sm shadow-lg ring-1 ring-black/5 rounded-xl gap-6 dark:highlight-white/5 mr-5 z-10">
                            <div class="py-3 pl-5 pr-5">
                                <NuxtLink to="/auth/logout">
                                    <a href="#" class="font-semibold text-gray-900 hover:text-gray-900">
                                        Logout
                                    </a>
                                </NuxtLink>
                            </div>
                        </div>

                    </div>

                </nav>



            </header>

            <section class="presentation-content">

                <article>
                    <h1 class="landing-title">
                        Cooking<br />
                        <span class="shift-name">Planner</span>
                    </h1>

                    <h2 class="text-2xl">{{ $t('home_page.presentation_section.slogan') }}</h2>
                    <p class="pt-5">{{ $t('home_page.presentation_section.explain') }}</p>

                    <div
                        class="inline-block mt-5 white-button max-w-sm shadow-lg ring-1 ring-black/5 rounded-xl gap-6 dark:highlight-white/5 z-10">
                        <div class="py-3 pl-5 pr-5">
                            <NuxtLink to="/generate">
                                Give it a try!
                            </NuxtLink>
                        </div>
                    </div>
                
                </article>

                <article class="absolute bottom-0 right-0">
                    <img class="object-right-bottom mr-20" src="@/assets/images/home/mama.svg" alt="Cooking person"
                        width="400px" />
                </article>

            </section>

        </div>
    </div>
</template>

<style scoped>
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

.presentation-background {
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

.presentation-content-layer {
    padding-left: 100px;
    padding-right: 100px;
    padding-top: 10px;
}

h1.landing-title {
    font-size: 80px;
    line-height: 80px;
    padding-bottom: 30px;
}

h1.landing-title>.shift-name {
    padding-left: 50px;
}


.presentation-content {
    padding-top: 50px;
    width: 700px;
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
