<template>
    <!--Cpu Usage-->
    <LineChart v-if="jsonData.length > 0" :data="jsonData[0]" color="blue" />
    <!--Cpu Temp-->
    <LineChart v-if="jsonData.length > 0" :data="jsonData[1]" color="blue" />
</template>
<script setup>
    import { ref } from 'vue';
    import LineChart from './components/LineChart.vue'

    const jsonData = ref([]);
    
    async function fetchData(){
        jsonData.value = await fetch('http://127.0.0.1:5000/api/stats')
        .then(data => data.json());
        console.log(jsonData.value[0]);
    }
    fetchData();
</script>
<style>

</style>