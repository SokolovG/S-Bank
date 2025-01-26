<script>
    import "../app.css"
    import { Header, Footer } from "$lib"
</script>
  

<div class="app min-h-screen bg-[#b44b28] flex flex-col">
  <Header />
  <main class="flex-grow">
    <slot/>
  </main>
  <Footer />
</div>