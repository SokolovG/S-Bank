<script>
    import { EventCard } from "$lib";
</script>
<div class="min-h-screen bg-gray-50">
    <!-- Profile Header -->
    <div class="bg-white border-b">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="flex flex-col md:flex-row gap-6 items-start">
          <!-- Avatar and Basic Info -->
          <div class="flex-shrink-0">
            <div class="w-32 h-32 rounded-full bg-gray-200 flex items-center justify-center">
              <svg class="w-16 h-16 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
          </div>
  
          <div class="flex-grow">
            <h1 class="text-2xl font-bold text-gray-900 mb-2">John Doe</h1>
            <p class="text-gray-600 mb-4">Software Developer | Tech Enthusiast</p>
            
            <div class="flex flex-wrap gap-4">
              <div class="flex items-center text-gray-600">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                john.doe@example.com
              </div>
              <div class="flex items-center text-gray-600">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                San Francisco, CA
              </div>
            </div>
          </div>
  
          <div class="flex-shrink-0">
            <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
              Edit Profile
            </button>
          </div>
        </div>
      </div>
    </div>
  
    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Navigation Tabs -->
      <div class="border-b mb-8">
        <nav class="flex space-x-8">
          <button class="px-1 py-4 text-sm font-medium text-blue-600 border-b-2 border-blue-600">
            Upcoming Events
          </button>
          <button class="px-1 py-4 text-sm font-medium text-gray-500 hover:text-gray-700">
            Past Events
          </button>
        </nav>
      </div>
  
      <!-- Events Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        <!-- Event Card -->
        <EventCard />
        <!-- Add more event cards as needed -->
      </div>
  
      <!-- Statistics Section -->
      <div class="mt-12 grid grid-cols-1 md:grid-cols-4 gap-6">
        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-4xl font-bold text-blue-600 mb-2">12</div>
          <div class="text-sm text-gray-600">Events Attended</div>
        </div>
        
        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-4xl font-bold text-blue-600 mb-2">4</div>
          <div class="text-sm text-gray-600">Upcoming Events</div>
        </div>
    
        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-4xl font-bold text-blue-600 mb-2">95%</div>
          <div class="text-sm text-gray-600">Attendance Rate</div>
        </div>
      </div>
    </div>
  </div>