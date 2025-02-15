<script lang="ts">
    import { HomepageCard, HomepageCategory } from "$lib";
</script>
<!-- Hero Section -->
<section class="bg-gradient-to-r from-blue-50 to-indigo-50 py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
            <h1 class="text-4xl font-bold text-gray-900 mb-4">
                Find Your Next Tech Conference
            </h1>
            <p class="text-xl text-gray-600 mb-8">
                Discover upcoming IT events, conferences, and meetups worldwide
            </p>
            <!-- Search Box -->
            <div class="max-w-2xl mx-auto">
                <div class="flex gap-4 p-2 bg-white rounded-lg shadow-sm">
                    <input type="text" 
                           placeholder="Search for conferences..." 
                           class="flex-grow px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <button class="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
                        Search
                    </button>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Featured Conferences -->
<section class="py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Upcoming Conferences</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"></div>
    </div>
    <HomepageCard />
</section>


<!-- Categories Section -->
<section class="py-12 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Browse by Category</h2>
            <HomepageCategory />
    </div>
</section>


<!-- CTA Section -->
<section class="py-12 bg-blue-600">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-2xl font-bold text-white mb-4">Are you organizing a tech conference?</h2>
        <p class="text-blue-100 mb-8 max-w-2xl mx-auto">
            List your event on our platform and reach thousands of potential attendees
        </p>
        <button class="px-8 py-3 bg-white text-blue-600 rounded-md font-semibold hover:bg-blue-50">
            Add Your Event
        </button>
    </div>
</section>