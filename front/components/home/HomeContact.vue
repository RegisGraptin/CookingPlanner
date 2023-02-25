<template>

    <section class="contact-section">

        <article class="container mx-auto py-5 pl-5">

            <h2>Get started</h2>

            <h3 class="text-4xl">Enter your e-mail address<br />
                and be one of the first to use it!</h3>

            <form class="flex items-center">

                <div class="relative mb-6 pr-2">
                    <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path>
                            <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path>
                        </svg>
                    </div>
                    <input type="text" id="input-group-1"
                        class="email-input border border-gray-300 text-sm rounded-lg block w-full pl-10 p-2.5"
                        placeholder="Your email address...">
                </div>

                <div class="mb-6">
                    <button data-element="submit">
                        <span class="cursor-pointer text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-3 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Subscribe</span>
                    </button>
                </div>



            </form>

        </article>
    </section>

</template>
<style scoped>
.contact-section {
    background-color: #febd2e;
    padding-top: 50px;
    padding-bottom: 50px;
    padding-left: 100px;
}

.email-input {
    background-color: white;
    width: 300px;
}

h3 {
    padding-top: 20px;
    padding-bottom: 30px;
}

</style>