<script>
    import "../app.css"
    import { Header, Footer } from "$lib"
</script>
  

<div class="app min-h-screen bg-[#2A2B2E] flex flex-col">
  <Header />
  <main class="flex-grow">
    <slot/>
  </main>
  <Footer />
</div>