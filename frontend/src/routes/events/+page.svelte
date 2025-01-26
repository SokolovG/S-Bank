<script lang="ts">
    import { onMount } from "svelte";
    import type { Event } from '$lib/types/events.ts';
    import EventCard from '$lib/components/EventCard.svelte';
    
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
    <div class="container mx-auto px-4 mt-8">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {#each events as event}
                <EventCard {event}/>
            {/each}
        </div>
    </div>
</main>

<style>
</style>