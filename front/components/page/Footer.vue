<template>
    <footer class="p-4 bg-white shadow md:px-6 md:py-8 dark:bg-gray-900">
        <div class="container mx-auto">
            <div class="sm:flex sm:items-center sm:justify-between">
                
                <NuxtLink to="/" class="flex items-center mb-4 sm:mb-0">
                    <!-- <img src="" class="h-8 mr-3" alt="Cooking Planner Logo" /> -->
                    <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">
                        Cooking Planner
                    </span>
                </NuxtLink>
                
                <ul class="flex flex-wrap items-center justify-end mb-6 text-sm text-gray-500 sm:mb-0 dark:text-gray-400">
                    <li>
                        <a href="#" class="mr-4 hover:underline md:mr-6 ">About</a>
                    </li>
                    <li>
                        <a href="#" class="mr-4 hover:underline md:mr-6">Privacy Policy</a>
                    </li>
                    <li>
                        <a href="#" class="mr-4 hover:underline md:mr-6 ">Licensing</a>
                    </li>
                    <li>
                        <a href="#" class="hover:underline">Contact</a>
                    </li>
                </ul>
            </div>

            <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
            <span class="block text-sm text-gray-500 sm:text-center dark:text-gray-400">&copy; {{ new Date().getFullYear()
            }}
                <NuxtLink to="/" class="hover:underline">Cooking Planner</NuxtLink>. All Rights Reserved.
            </span>

        </div>
    </footer>
</template>

<style scoped>
footer {
    background-color: #333333;
}
</style>