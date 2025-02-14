<template>
    <div v-for="{name, index} in stats" :key="index">
        <h3>Entry {{ index + 1 }}</h3>
    </div>
</template>

<script setup>
   import { ref, onMounted } from 'vue';

    const stats = ref([]);
    const fetchStats = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/stats');
            const data = await response.json();
            stats.value = data;
        } catch (error) {
            console.error('Error fetching stats:', error);
        }
    };

    onMounted(() => {
        fetchStats();
    });
</script>

<style scoped></style>