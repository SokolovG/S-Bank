<script lang="ts">
    import type { Event } from '$lib/types/events';
    export let event: Event;
</script>

<div class="border-2 border-solid border-gray-800 bg-white p-4 w-80 rounded-xl">
    <h3 class="text-xl font-bold mb-3">
    {event.name}
    </h3>
    
    <div class="space-y-3 mb-4">
    <div class="flex items-center ">
        <span class="text-sm">{event.eventStartDate}</span>
    </div>
    
    <div class="flex items-center ">
        <span class="text-sm">{event.eventEndDate}</span>
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
    
    <div class="pt-4 border-t border-gray-100">
    <button class="w-full bg-blue-500 text-white py-2 px-4 rounded-lg">
        Зарегистрироваться
    </button>
    </div>
</div>