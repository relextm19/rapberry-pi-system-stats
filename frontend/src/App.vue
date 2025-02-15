<template>
    <div v-for="stat in stats" :key="stat">
        <graph :data="stat"></graph>
        <p>Cwel</p>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import graph from './components/graph.vue';

    const stats = ref([]);
    const fetchStats = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/stats');
            const data = await response.json();
            stats.value = data;
            console.log(data)
        } catch (error) {
            console.error('Error fetching stats:', error);
        }
    };

    onMounted(() => {
        fetchStats();
    });
</script>

<style scoped></style>