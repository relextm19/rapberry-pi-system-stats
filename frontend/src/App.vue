<template>
    <div>
      <!-- CPU Graphs -->
      <Graph v-if="cpu_usage.length" :data="cpu_usage" title="CPU Usage (%)" color="blue" />
      <Graph v-if="cpu_temp.length" :data="cpu_temp" title="CPU Temperature (°C)" color="red" />
  
      <!-- Memory Graphs -->
      <Graph v-if="memory_total.length" :data="memory_total" title="Total Memory" color="green" />
      <Graph v-if="memory_available.length" :data="memory_available" title="Available Memory" color="lightgreen" />
      <Graph v-if="memory_percent.length" :data="memory_percent" title="Memory Usage (%)" color="darkgreen" />
      <Graph v-if="memory_used.length" :data="memory_used" title="Used Memory" color="olive" />
  
      <!-- Disk Graphs -->
      <Graph v-if="disk_total.length" :data="disk_total" title="Total Disk" color="purple" />
      <Graph v-if="disk_used.length" :data="disk_used" title="Used Disk" color="magenta" />
      <Graph v-if="disk_free.length" :data="disk_free" title="Free Disk" color="pink" />
      <Graph v-if="disk_percent.length" :data="disk_percent" title="Disk Usage (%)" color="violet" />
  
      <!-- Network Graphs -->
      <Graph v-if="network_bytes_sent.length" :data="network_bytes_sent" title="Network Bytes Sent" color="orange" />
      <Graph v-if="network_bytes_recv.length" :data="network_bytes_recv" title="Network Bytes Received" color="cyan" />
      <Graph v-if="network_packets_sent.length" :data="network_packets_sent" title="Network Packets Sent" color="brown" />
      <Graph v-if="network_packets_recv.length" :data="network_packets_recv" title="Network Packets Received" color="grey" />
  
      <!-- Uptime -->
      <Graph v-if="uptime.length" :data="uptime" title="Uptime" color="black" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import Graph from './Graph.vue';
  
  // CPU
  const cpu_temp = ref([]);
  const cpu_usage = ref([]);
  
  // Memory – assuming order: [total, available, percent, used]
  const memory_total     = ref([]);
  const memory_available = ref([]);
  const memory_percent   = ref([]);
  const memory_used      = ref([]);
  
  // Disk – assuming order: [total, used, free, percent]
  const disk_total   = ref([]);
  const disk_used    = ref([]);
  const disk_free    = ref([]);
  const disk_percent = ref([]);
  
  // Network – assuming order: [bytes_sent, bytes_recv, packets_sent, packets_recv]
  const network_bytes_sent   = ref([]);
  const network_bytes_recv   = ref([]);
  const network_packets_sent = ref([]);
  const network_packets_recv = ref([]);
  
  // Uptime
  const uptime = ref(0);
  
  /**
   * Extracts the metrics from each data object and accumulates the values.
   * We assume each incoming object from the API follows the structure:
   * {
   *    cpu_percent: number,
   *    cpu_temperature: number,
   *    memory_stats: [total, available, percent, used],
   *    disk_stats: [total, used, free, percent],
   *    network_io: [bytes_sent, bytes_recv, packets_sent, packets_recv],
   *    uptime: number
   * }
   */
  const extractMetrics = (dataArray) => {
    if (!dataArray || dataArray.length === 0) return;
    dataArray.forEach(item => {
      cpu_temp.value.push(item.cpu_temp);
      cpu_usage.value.push(item.cpu_usage);
      uptime.value = item.uptime;
  
      // Memory values
      if (Array.isArray(item.memory_stats) && item.memory_stats.length >= 4) {
        const [memTotal, memAvailable, memPercent, memUsed] = item.memory_stats;
        memory_total.value.push(memTotal);
        memory_available.value.push(memAvailable);
        memory_percent.value.push(memPercent);
        memory_used.value.push(memUsed);
      }
  
      // Disk values
      if (Array.isArray(item.disk_stats) && item.disk_stats.length >= 4) {
        const [dTotal, dUsed, dFree, dPercent] = item.disk_stats;
        disk_total.value.push(dTotal);
        disk_used.value.push(dUsed);
        disk_free.value.push(dFree);
        disk_percent.value.push(dPercent);
      }
  
      // Network values (note: your original code names this network_stats, but your API returns 'network_io')
      if (Array.isArray(item.network_io) && item.network_io.length >= 4) {
        const [netSent, netRecv, netPacketsSent, netPacketsRecv] = item.network_io;
        network_bytes_sent.value.push(netSent);
        network_bytes_recv.value.push(netRecv);
        network_packets_sent.value.push(netPacketsSent);
        network_packets_recv.value.push(netPacketsRecv);
      }
    });
  };
  
  const fetchStats = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/stats');
      const data = await response.json();
      extractMetrics(data);
      console.log('CPU Temperature Data:', cpu_temp.value);
    } catch (error) {
      console.error('Error fetching stats:', error);
    }
  };
  
  onMounted(fetchStats);
  </script>
  