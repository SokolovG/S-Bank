<script lang="ts">
    import { onMount } from "svelte";
    import type {Event} from '$lib/types/events';

    let events: Event[] = [];

    async function fetchEvents() {
        try {
            const response = await fetch('http://localhost:8000/api/events/');
            const data: Event[] = await response.json();
            events = data;
            console.log(events);
        } catch (error) {
            console.log(error)
        } 
    }

    onMount(() => {
        fetchEvents();
    })
</script>

<main>
    <div>
        <ul>
            {#each events as event (event)}
                <li>{event.name}</li>
            {/each}
        </ul>
    </div>
</main>

<style>
</style>