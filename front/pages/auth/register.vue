<template>
    <section class="flex flex-col md:flex-row h-screen items-center">

        <section class="bg-white w-full md:max-w-md lg:max-w-full md:mx-auto md:mx-0 md:w-1/2 xl:w-1/3 h-screen px-6 lg:px-16 xl:px-12
        flex items-center justify-center">
            <RegisterForm />
        </section>

        <div class="bg-indigo-600 hidden lg:block w-full md:w-1/2 xl:w-2/3 h-screen">
            <img src="@/static/auth/cooking.jpg" alt="" class="w-full h-full object-cover">
        </div>

    </section>
</template>
  
<script>

import RegisterForm from '~/components/auth/RegisterForm.vue';

export default {
    name: 'RegisterPage',
    components: { RegisterForm },
}
</script>
  