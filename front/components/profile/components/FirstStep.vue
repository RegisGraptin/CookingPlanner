<template>

    <section>
        <h1>Step 1</h1>


        <!-- Number of persons -->
        <h3>Number of persons</h3>
        <article class="flex items-center justify-around w-1/2 mx-auto">

            <div style="width: 50px;">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth=1.5 stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
                </svg>
            </div>

            <button class="text-xl" @click="removePerson">-</button>


            <p class="text-xl">{{ profile.n_persons }}</p>

            <button class="text-xl" @click="addPerson">+</button>

            <div style="width: 50px;">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197M15 6.75a3 3 0 11-6 0 3 3 0 016 0zm6 3a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0zm-13.5 0a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z" />
                </svg>
            </div>

    </article>

    </section>

</template>

<script>

export default {
    name: "",
    props: {
        profile: Object
    },
    methods: {
        addPerson() {
            this.$log.debug("Add a person");
            if (this.profile.n_persons < 10) {
                this.profile.n_persons++;   
            }
        },
        removePerson() {
            this.$log.debug("Remove a person");
            if (this.profile.n_persons > 1) {
                this.profile.n_persons--;   
            }
        }
    }
}
</script>
