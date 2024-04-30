<template>
  <div class="box">
    <el-row :gutter="20">
      <el-col :span="3" v-for="n in 60" :key="n">
        <div class="grid-content-wrapper">
          <div class="grid-content">
            <div>+0010.000 V</div>
            <div>+0100.000 mA</div>
            <div>+1000.000 mW</div>
            <!-- <div class="slider-demo-block">
              <el-slider v-model="value" show-input size="small" />
            </div> -->
            <div class="slider-demo-block">
                <el-slider v-model="value" size="small" />
                <el-input-number v-model="value1" :min="0" :max="100" size="small" />
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref } from "vue";
const value = ref(0);

</script>

<style scoped>
.box {
  width: 100%;
  height: 100%;
  padding: 20px;
  box-sizing: border-box;
}
/* Layout */
.el-col {
  margin-bottom: 20px;
  box-sizing: border-box;
  border-radius: 8px;
}
.grid-content-wrapper {
  padding-top: 75%; /* Height is 75% of the width, which makes the aspect ratio 4:3 */
  position: relative;
  width: 100%;
}
.grid-content {
  border-radius: 4px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border: 1px solid #ccc;
  background-color: #ccc;
  padding: 10px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}


/* Slider */
.slider-demo-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px;
}

/* .slider-demo-block {
width: 100%;
  max-width: 600px;
  display: flex;
  flex: 1;
  align-items: center;
  justify-content: center;
}
.el-slider {
  width: 100%; 
  margin-top: 10px; 
  display: flex;
  flex-direction: column;
  align-items: center; 
}

.grid-content .slider-demo-block .el-slider {
  display: block;
  box-sizing: border-box;
}
.el-slider--small {
  height: 100%;
}
.el-slider__runway.show-input {
    margin: 0;
} */

</style>