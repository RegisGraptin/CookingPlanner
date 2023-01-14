<template>

    <div class="presentation_background">
        <div class="">
            <v-container>
            <header id="logo">
                <h1>Cooking Planner</h1>
            </header>

            <div class="container">
                <div class="presentation_content">
                    <h1 class="pb-2">Cooking Planner</h1>

                    <h2 class="pb-3">Slogan</h2>
                    <p>first title description</p>
                    <p>Call back email</p>

                    <p>
                        <NuxtLink to="/generate">
                            Generate your next week
                        </NuxtLink>
                    </p>

                </div>
            </div>
        </v-container>
        </div>

    </div>
</template>

<style>

.presentation_background {
    height: 500px;
    background-color: #FEBD2E;
    

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

.presentation_gradient_colors {
    width: 100%;
    height: 100%;
    /* // background: rgba(2, 0, 36, 0.6); */
    background-image: linear-gradient(
        to right bottom, 
        rgba(3,0,61,0.4), 
        rgba(24,20,87,0.5), 
        rgba(49,36,113,0.5), 
        rgba(73,53,141,0.5), 
        rgba(98,71,170,0.5)
    );
    color: white;
}

.presentation_content {
    padding-top: 200px;
    width: 600px;
    left: 0;
    position: relative;
    z-index: 100;
}

.content-inputs .vs-input {
    width: 300px;
}


.image-color-gradient {
    background-image: linear-gradient(to right bottom, #03003d, #181457, #312471, #49358d, #6247aa);
    width: 100%;
    height: 100%;
    border-radius: 20px;
    /* // box-shadow: -5px 5px 5px rgba(31,45,65,.15);;
    // box-shadow: -5px 5px 5px blue; */
}

.image-color-gradient > img {
    opacity: 0.5;
    border-radius: 20px;
    filter: drop-shadow(0 0 10rem grey);
}

.bg-grey {
    background-color: #F3F5F7 !important;
}

.fullpage {
    min-height: 100vh;
}

.product-feature {
    box-shadow: 0 .15rem 1.75rem 0 rgba(31,45,65,.15);
    transform: translateZ(0);
    transition-duration: 6s;
    transition-property: opacity,transform,-webkit-transform;
    /* // animation: slide-in 0.5s forwards;
    // -webkit-animation: slide-in 0.5s forwards; */
    border-radius: 20px;
}

.product-feature h2.card-title {
    font-size: 30px;
    letter-spacing: 0.2em;
    font-family: Comfortaa, sans-serif;
    
    
}


.product-feature p.card-text {
    color: #6c757d;
    font-size: 18px;
    text-align: justify;
}




.features-container {
    position: relative;
    padding-bottom: 50px;
}

.features-container > section > section {
    z-index: 1;
    border: none;
}

.background-svg-transition > svg {
    position: absolute;
    bottom: 0;
    z-index: 0;
}

</style>

<script>
export default {}
</script>
