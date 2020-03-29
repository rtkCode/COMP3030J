<template>
    <div>
        <HeaderIn v-if="$token.hasToken()" :hospital="hospital"></HeaderIn>
        <Header v-else :hospital="hospital"></Header>
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
            hospital: String
        },
    };
</script>