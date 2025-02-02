<script>
    import { goto } from "$app/navigation"
</script>

<div class="container mx-auto mt-8 px-4">

    <h1 class="text-4xl font-bold text-center mb-8">Welcome to DevEvents</h1>
    

    <p class="text-xl text-gray-600 text-center mb-12">Choose your path to connect with the tech community</p>
    

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 py-4">
        <a href="/events" class="block">
            <div class="border-2 border-gray-900 rounded-xl p-8 hover:bg-gray-400 transition-colors duration-300 cursor-pointer">
                <div class="flex flex-col items-center justify-center min-h-[200px]">
                <h2 class="text-3xl font-semibold mb-4">For Members</h2>
                <p class="text-gray-600 text-center text-lg">
                    Discover tech events, join communities, and grow your network
                </p>
                </div>
            </div>
        </a>

        
    

        <a href="/organizers" class="block">
            <div class="border-2 border-gray-900 rounded-xl p-8 hover:bg-gray-400 transition-colors duration-300 cursor-pointer">
                <div class="flex flex-col items-center justify-center min-h-[200px]">
                    <h2 class="text-3xl font-semibold mb-4">For Organizers</h2>
                    <p class="text-gray-600 text-center text-lg">
                        Create and manage your tech events, reach your target audience
                    </p>
                </div>
            </div>
        </a>
        
    </div>
</div>