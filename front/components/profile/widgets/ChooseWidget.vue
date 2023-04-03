<template>
    <article class="mt-5">

        <h2 class="text-center pt-5 mb-5 text-lg font-medium text-gray-900">{{ title }}</h2>

        <div class="flex items-center justify-around w-2/3 mx-auto">

            <ul :class="'grid w-full gap-6 md:grid-cols-' + nb_items">

                <li v-for="(item, index) in items">

                    <input v-model="variable[key_name]" type="radio" :name="key_name" :id="key_name + '-' + index"
                        :value="item.value" class="hidden peer">

                    <label :for="key_name + '-' + index"
                        class="inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer peer-checked:border-blue-600 peer-checked:text-blue-600 hover:text-gray-600 hover:bg-gray-100 ">

                        <div class="block">
                            <div class="w-full text-lg font-semibold">{{ item.name }}</div>
                        </div>

                        <img v-if="item.icon" :src="require(`~/assets/images/${item.icon}`)" width="64" height="64" />

                        <svg v-else aria-hidden="true" class="w-6 h-6 ml-3" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                                clip-rule="evenodd"></path>
                        </svg>
                    </label>
                </li>

            </ul>
        </div>
    </article>
</template>

<script>
export default {
    name: "test",
    props: {
        key_name: String,
        variable: Object,
        items: Array,
        title: String,
    },
    data() {
        return {
            nb_items: this.items.length,
        }
    }
}
</script>