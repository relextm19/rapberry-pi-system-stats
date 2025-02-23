<template>
    <div class="graph-container">
      <h2>{{ title }}</h2>
      <Line v-if="flatData.length" :data="chartData" />
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
    title: String, // Title of the graph
    color: String  // Line color
  });
  
  // Create a computed property that flattens the data if needed.
  const flatData = computed(() => {
    // If the first element is an array, flatten the entire data array.
    return Array.isArray(props.data[0]) ? props.data.flat() : props.data;
  });
  
  const chartData = computed(() => ({
    // Generate labels based on the flat data length.
    labels: flatData.value.map((_, i) => `${i + 1}s`),
    datasets: [
      {
        label: props.title,
        data: flatData.value,
        borderColor: props.color,
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
  