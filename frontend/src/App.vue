<template>
    <h1> {{ name }}</h1>
    <p v-if="status === 'active'"> User is active</p>
    <p v-else-if="status==='inactive'">User is inactive</p>
    <p v-else> User is a fucking moron</p>
    <h3>Tasks:</h3>
    <ul>
        <li v-for="task in tasks" :key="task">{{ task }}</li>
    </ul>

    <a :href="link">Click for candy</a>
    <button @click="change_status">Change user status</button>
</template>

<script>
    export default {
        data() {
            return {
                name: 'John Doe',
                status: 'active',
                tasks: ['task1', 'task2', 'task3'],
                link: 'https://youtube.com',
            }
        },
        methods: {
            change_status(){
                if(this.status ==='active'){
                    this.status ='inactive';
                } else if(this.status === 'inactive'){
                    this.status = 'active';
                }
            }
        }
    }   
</script>

<style scoped></style>