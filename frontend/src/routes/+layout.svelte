<script>
    import "../app.css"
    import {Header, Footer } from "$lib"
</script>
  

<div class="app">
  <Header />
  <main>
    <slot/>
  </main>
  <Footer />
</div>