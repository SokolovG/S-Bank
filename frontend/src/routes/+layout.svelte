<script>
    import "../app.css"
    import { Header, Footer } from "$lib"
</script>

<!DOCTYPE html>
<html lang="ru" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT Conference Aggregator</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="flex flex-col min-h-full bg-gray-50">
    <!-- Header -->
  <Header />
    <!-- Main Content -->
    <main class="flex-grow">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <slot />
            </div>
    </main>
    <!-- Footer -->
    <Footer />
</body>
</html>