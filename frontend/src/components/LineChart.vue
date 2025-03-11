<template>
    <div class="graph-container"> 
        <Line v-if="chartData" :data="chartData" :options="chartOptions"/>
    </div>
</template>

<script setup>
    import { computed } from 'vue';
    import { Line } from 'vue-chartjs';
    import {
        Chart as ChartJS,
        CategoryScale, 
        LinearScale,
        PointElement,
        LineElement,
        Title,
        Tooltip,
        Legend
    } from 'chart.js';

    ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

    const props = defineProps({
        data: Array,   // Data points for the graph
        color: String  // Line color
    });

    const chartTitle = computed(() => props.data[0]); //first row is the title of the graph

    const chartData = computed(() => ({
        labels: props.data.slice(1).map((_, i) => `${i + 1}s`), // Generate labels (1s, 2s, ...)
        datasets: [
            {
                label: chartTitle.value,
                data: props.data.slice(1), 
                borderColor: props.color || 'blue',
                fill: false
            }
        ]
    }));
    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false, // stretch the graph across the whole container
        scales: {
            x: {
                ticks: {
                    color: "#f0f0f0",
                },
            },
            y: {
                ticks: {
                    color: "#f0f0f0",
                },
            },
        },
    };
</script>

<style scoped>
   
</style>
