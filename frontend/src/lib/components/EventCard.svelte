<script lang="ts">
    import type { Event } from '$lib/types/events';
    import { formatEventDate } from "$lib/utils/date.js"
    export let event: Event;
</script>

<div class="border-solid bg-[#ffd7b9] p-4 w-75 rounded-xl">
    <h3 class="text-xl font-bold mb-3">
    {event.name}
    </h3>
    
    <div class="space-y-3 mb-4">
    <div class="flex items-center ">
        <span class="text-sm">{formatEventDate(event.eventStartDate)}</span>
    </div>
    
    <div class="flex items-center ">
        <span class="text-sm">{event.location.name}</span>
    </div>
    
    <div class="flex items-center ">
        <span class="text-sm">{event.maxParticipants} участников</span>
    </div>
    </div>
    
    <p class=" text-sm mb-4">
    {event.description}
    </p>
    
</div>