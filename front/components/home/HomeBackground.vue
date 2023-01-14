<template>

    <div class="presentation_background">
        <div class="">
            <v-container>

            <header id="logo">

                <nav class="flex flex-row" id="top-menu">

                    <div class="flex content-center" id="menu-nav-links">
                        <h1 id="menu-title font-semibold">Cooking Planner</h1>

                        <div class="flex space-x-4 nav-links">
                            <a href="#" class="font-semibold">Home</a>
                            <a href="#" class="font-semibold">Features</a>
                            <a href="#" class="font-semibold">Contact</a>
                        </div>
                    </div>

                    <div>
                        <a href="#" class="font-semibold text-gray-900 hover:text-gray-900">Login</a>
                        <a href="#" class="font-semibold text-gray-900 hover:text-gray-900">Sign up</a>
                    </div>

                </nav>



            </header>

            <section class="presentation_content">
            
                <h1 class="landing-title">
                    Cooking<br/>
                    <span class="shift-name">Planner</span>
                </h1>

                <p>The new way to organize your cooking week.</p>
                <p>Help you to organize your week</p>

                <p>
                    <NuxtLink to="/generate">
                        Generate your next week
                    </NuxtLink>
                </p>

            </section>
        
        </v-container>
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

nav#top-menu, #menu-nav-links {
    align-items: center; 
}

.nav-links > a {
    padding-left: 30px;
    color: #333333b3;
}
.nav-links > a:hover {
    color: #333333;
}

.presentation_background {
    height: 500px;    
    background-color: #febd2e;


    margin-left:  7px;
    margin-right: 7px;
    margin-top:   7px;

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

h1.landing-title > .shift-name {
    padding-left: 50px;
}


.presentation_content {
    padding-top: 50px;
}


</style>

<script>
export default {}
</script>
