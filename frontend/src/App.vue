<template>
    <Uptime :uptime="uptime" />
    <div class="f-wrapper">
        <h1>CPU</h1>
    </div>
    <div class="graphs-container">
        <!--Cpu Usage-->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="cpuStats[0]" color="blue" />
        <!--Cpu Temp-->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="cpuStats[1]" color="blue" />
    </div>
    <div class="f-wrapper">
        <h1>RAM</h1>
    </div>
    <div class="graphs-container">
        <!--Free Memory -->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="memoryStats[0]" color="blue" />
        <!--Memory Used-->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="memoryStats[1]" color="blue" />
        <!-- Memory Percentage -->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="memoryStats[2]" color="blue" />
    </div>
    <div class="f-wrapper">
        <h1>NETWORK</h1>
    </div>
    <div class="graphs-container wrap">
        <!-- Bytes Sent -->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="networkStats[0]" color="blue" />
        <!-- Bytes Received -->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="networkStats[1]" color="blue" />
        <!-- Packets Sent -->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="networkStats[2]" color="blue" />
        <!-- Packets Received -->
        <LineChart class="chart" v-if="jsonData.length > 0" :data="networkStats[3]" color="blue" />
    </div>
</template>
<script setup>
    import { ref } from 'vue';
    import LineChart from './components/LineChart.vue'
    import Uptime from './components/Uptime.vue';

    const jsonData = ref([]);

    const uptime = ref();
    const cpuStats = ref([]);
    const memoryStats = ref([]);
    const networkStats = ref([]);
    
    async function fetchData(){
        jsonData.value = await fetch('http://127.0.0.1:5000/api/stats')
        .then(data => data.json());
        uptime.value = jsonData.value.at(-1).at(-1);
        cpuStats.value = splitData(['percentage used', 'temperature'], jsonData.value[0]);
        memoryStats.value = splitData(['free memory', 'percentage used', 'used memory'], jsonData.value[1]);
        networkStats.value = splitData(['bytes_sent', 'bytes_received', 'packets_sent', 'packets_received'], jsonData.value[2]);
    }
    fetchData();
</script>
<script>
    function formatTime(time){
        const hours = (time / 3600).toFixed(0).padStart(2, '0');
        const minutes = ((time / 60) % 60).toFixed(0).padStart(2, '0');
        const seconds = (time % 60).toFixed(0).padStart(2, '0');

        return `${hours}:${minutes}:${seconds}`;
    }

    function splitData(headers, rawData){
        const columnCount = headers.length;
        const result = Array.from({ length: columnCount }, (_, i) => [headers[i]]); // Create an array of arrays with headers

        rawData.shift(); // Remove the first element which is the header

        for (let row of rawData) {
            for (let i = 0; i < columnCount; i++) {
                result[i].push(row[i]);
            }
        }

        return result;
    }
</script>
<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        color: white;
    }
    
    .f-wrapper {
        text-align: center;
        margin-bottom: 20px;
    }
    .f-wrapper h1 {
        font-size: 1.5rem;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    .f-wrapper h2.uptime {
        font-size: 1.25rem;
        font-weight: 400;
    }

    .graphs-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
    }

    .wrap {
        flex-wrap: wrap;
    }

    .chart {
        width: 100%;
        height: 250px; /* Set a fixed height for all charts */
        background: #2c2c2c;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    @media (max-width: 768px) {
        .graphs-container {
            grid-template-columns: 1fr; /* Stack charts on smaller screens */
        }
    }
</style>
