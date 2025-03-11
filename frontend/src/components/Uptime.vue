<template>
    <div class="uptime-container">
        <h1 class="uptime-title">Uptime</h1>
        <div class="uptime-display">
            {{ formatTime(uptime) }}
        </div>
    </div>
</template>

<script setup>
    const props = defineProps({
        uptime: {
            type: Number,
            required: true
        }
    });

    function formatTime(time) {
        const hours = (time / 3600).toFixed(0).padStart(2, '0');
        const minutes = ((time / 60) % 60).toFixed(0).padStart(2, '0');
        const seconds = (time % 60).toFixed(0).padStart(2, '0');
        return `${hours}:${minutes}:${seconds}`;
    }
</script>

<style scoped>
    *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    .uptime-container {
        margin: 20px auto;
        border-radius: 8px;
        max-width: 200px;
        height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }

    .uptime-title {
        font-size: 1.8rem;
        margin-bottom: 10px;
        font-weight: 600;
        color: #f0f0f0;
    }

    .uptime-display {
        font-size: 1.5rem;
        font-weight: 500;
        padding: 10px 20px;
        border: 1px solid #FFFFFF;
        border-radius: 4px;
        background-color: #1a1a1a;
        color: #ffffff;
        display: inline-block;
    }
</style>
