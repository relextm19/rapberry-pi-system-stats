<template>
    <div>
        <Line :data="data" />
    </div>
</template>
<script setup>
    import { onMounted } from 'vue';
    import {
        Chart as ChartJS,
        CategoryScale,
        LinearScale,
        PointElement,
        LineElement,
        Title,
        Tooltip,
        Legend
    } from 'chart.js'
    import { Line } from 'vue-chartjs'
    import * as chartConfig from './chartConfig.js'

    ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

    const props = defineProps({
        chartData: Object
    })

    // Chart.js options
    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top'
            }
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
</script>

<style>

</style>