<script>
  import { goto } from "$app/navigation"
</script>

<header class="flex justify-between bg-gray-700 px-6 py-6 shadow">
  <div class="text-2xl font-bold text-[#FFFFFF] hover:text-red-900">
    <button on:click={() => goto('/')}>DevEvents</button>

  </div>
  
  <div class="flex space-x-6 text-[#FFFFFF] text-xl font-bold">
    <div class="hover:text-red-900 cursor-pointer">
      <button on:click={() => goto('/events')}>
        Events
      </button>
    </div>
    <div class="hover:text-red-900 cursor-pointer">Organizers</div>
    <div class="hover:text-red-900 cursor-pointer">About</div>
  </div>
  
  <div class="text-[#FFFFFF] text-xl font-bold hover:text-red-900 cursor-pointer">
    Log In
  </div>
</header>