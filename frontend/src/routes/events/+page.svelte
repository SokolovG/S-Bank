<script lang="ts">
    import { onMount } from "svelte";
    import type { Event, PaginatedResponse } from '$lib/types/events.ts';
    import EventCard from '$lib/components/EventCard.svelte';
    import { goto } from "$app/navigation"
    let events: Event[] = [];

    async function fetchEvents() {
        try {
            const response = await fetch('http://localhost:8000/api/events/');
            const data: PaginatedResponse = await response.json();
            events = data.results;
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
        <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-5 gap-8 py-14">
            {#each events as event}
                <a href="/events/{event.id}" class="block">
                    <EventCard {event}/>
                </a>
            {/each}
        </div>
    </div>
</main>

<style>
</style>