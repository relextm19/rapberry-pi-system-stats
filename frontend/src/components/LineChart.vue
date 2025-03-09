<template>
    <div class="graph-container"> 
        <h2>{{ props.data[0] }}</h2> <!-- First row is the graph title -->
        <Line v-if="chartData" :data="chartData" />
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
</script>

<style scoped>
    .graph-container {
        margin-bottom: 20px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 8px;
    }
</style>
