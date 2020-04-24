<template>
    <div>
        <HeaderIn v-if="$token.hasToken()" :hospital="hospital" :transparent="transparent" :type="type"></HeaderIn>
        <Header v-else :hospital="hospital" :transparent="transparent"></Header>
    </div>
</template>

<script>
    import Header from "@/components/Header.vue";
    import HeaderIn from "@/components/HeaderIn.vue";

    export default {
        components: {
            HeaderIn,
            Header,
        },
        props: {
            hospital: String,
            transparent: Boolean,
            type: String,
        },
    };
</script>