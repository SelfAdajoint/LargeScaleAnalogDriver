<script setup>
import Header from "@/components/header.vue";
import Voltstatus from "@/components/voltstatus.vue";
import Footer from "@/components/footer.vue";
import { ref } from 'vue'
const emitvalue= ref(true)
const isAlldisable = (isoff) => {
  emitvalue.value = isoff
}
</script>

<template>
  <div class="container">
    <Header devid="09df2712" @alldisable="isAlldisable"/>
    <div class="voltstatus">
      <Voltstatus devid="09df2712" :isoff="emitvalue" />
    </div>
    <div class="footer">
      <Footer />
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.voltstatus {
  flex: 1;
}
.footer {
  height: 40px;
}
</style>
