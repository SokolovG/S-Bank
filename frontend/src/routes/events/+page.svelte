<script>
    import { EventCard } from "$lib";
  </script>
  
  <div class="min-h-screen bg-gray-50">
    <!-- Header with search -->
    <div class="bg-white border-b">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <h1 class="text-2xl font-bold text-gray-900">All Events</h1>
          
          <!-- Search -->
          <div class="flex gap-2 w-full md:w-auto">
            <input type="text" 
                   placeholder="Search events..." 
                   class="px-4 py-2 border rounded-lg flex-grow md:w-80 focus:outline-none focus:ring-2 focus:ring-blue-500">
            <button class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
              Search
            </button>
          </div>
        </div>
      </div>
    </div>
  
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="grid grid-cols-12 gap-6">
        <!-- Sidebar with filters -->
        <div class="col-span-12 lg:col-span-3">
          <div class="bg-white rounded-lg shadow-sm p-4">
            <h2 class="font-semibold mb-4">Filters</h2>
            
            <!-- Format -->
            <div class="mb-6">
              <h3 class="text-sm font-medium text-gray-700 mb-2">Format</h3>
              <div class="space-y-2">
                <label class="flex items-center">
                  <input type="checkbox" class="rounded text-blue-600">
                  <span class="ml-2">Online</span>
                </label>
                <label class="flex items-center">
                  <input type="checkbox" class="rounded text-blue-600">
                  <span class="ml-2">In-person</span>
                </label>
              </div>
            </div>
  
            <!-- Status -->
            <div class="mb-6">
              <h3 class="text-sm font-medium text-gray-700 mb-2">Status</h3>
              <div class="space-y-2">
                <label class="flex items-center">
                  <input type="checkbox" class="rounded text-blue-600">
                  <span class="ml-2">Registration Open</span>
                </label>
                <label class="flex items-center">
                  <input type="checkbox" class="rounded text-blue-600">
                  <span class="ml-2">Coming Soon</span>
                </label>
              </div>
            </div>
  
            <!-- Price -->
            <div class="mb-6">
              <h3 class="text-sm font-medium text-gray-700 mb-2">Price</h3>
              <div class="space-y-2">
                <label class="flex items-center">
                  <input type="checkbox" class="rounded text-blue-600">
                  <span class="ml-2">Free</span>
                </label>
                <label class="flex items-center">
                  <input type="checkbox" class="rounded text-blue-600">
                  <span class="ml-2">Paid</span>
                </label>
              </div>
            </div>
          </div>
        </div>
  
        <!-- Events grid -->
        <div class="col-span-12 lg:col-span-9">
          <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            <!-- Event card 1 -->
            <EventCard />
          </div>
          
          <!-- Pagination -->
          <div class="mt-8 flex justify-center">
            <nav class="flex items-center gap-2">
              <button class="px-3 py-1 border rounded-lg hover:bg-gray-50">←</button>
              <button class="px-3 py-1 border rounded-lg bg-blue-600 text-white">1</button>
              <button class="px-3 py-1 border rounded-lg hover:bg-gray-50">2</button>
              <button class="px-3 py-1 border rounded-lg hover:bg-gray-50">3</button>
              <button class="px-3 py-1 border rounded-lg hover:bg-gray-50">→</button>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>