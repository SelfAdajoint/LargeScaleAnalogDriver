<template>
  <div class="box">
    <el-row :gutter="20">
      <el-col :span="3" v-for="n in 64" :key="n">
        <div class="grid-content-wrapper">
          <div class="grid-content">
            <div>+{{volt[n]}} V</div>
            <div>+0100.000 mA</div>
            <div>+1000.000 mW</div>
            <!-- <div class="slider-demo-block">
              <el-slider v-model="value" show-input size="small" />
            </div> -->
            <div class="slider-demo-block">
                <el-slider v-model="volt[n]" :min="0" :max="10" :step="0.001" size="small"
                  :format-tooltip="formatTooltip" @change="setvolt(n)"/>
                <el-input-number v-model="volt[n]" :min="0" :max="10" :precision="3" :step="0.001" size="small" />
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import axios from 'axios'

const props = defineProps(["devid",]);
const volt  = reactive(Array(64).fill(0));

function formatTooltip(number){
  return number.toFixed(3)
}

async function setvolt(n){
  const res = await axios.get(`http://127.0.0.1:6661/setvolt?devid=${props.devid}&ch=${n}&V=${volt[n]}`);
}

onMounted(() => {
  console.log(volt)
})

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
  width: 100%;
}
.grid-content {
  border-radius: 4px;
/*  position: absolute;*/
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  height: 110px;
  border: 1px solid #ccc;
  background-color: #ccc;
  padding: 10px;
  box-sizing: content-box;
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