<template>
  <div class="box">
    <el-row :gutter="20">
      <el-col :lg="3" :md="4" :sm="6" :xs="8" v-for="n in 64" :key="n">
        <div class="grid-content-wrapper">
          <div class="chnum">{{ n }}</div>
          <div class="grid-content">
            <div>+ {{ formatNumber(volt[n],8,3) }} V</div>
            <div>+ {{ formatNumber(amp[n],8,3) }} mA</div>
            <div>+ {{ formatNumber(volt[n]*amp[n],8,3) }} mW</div>
            <div class="slider-demo-block">
                <el-slider v-model="volt[n]" :min="0" :max="10" :step="0.001" size="small"
                  :format-tooltip="formatTooltip" @change="setvolt(n)"/>
                <el-input-number v-model="volt[n]" :min="0" :max="10" :precision="3" :step="0.001" size="small"
                  @change="setvolt(n)"/>
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
const volt  = reactive(Array(65).fill(0.0));
const amp   = reactive(Array(65).fill(100.0));

function formatTooltip(number){
  return number.toFixed(3)
}

function formatNumber(num, width, precision) {
  var formatted = num.toFixed(precision);
  var padding = width - formatted.length;
  if (padding > 0) {
      formatted = '0'.repeat(padding) + formatted;
  }
  return formatted;
}

async function setvolt(n){
  const res = await axios.get(`http://127.0.0.1:6661/setvolt?devid=${props.devid}&ch=${n}&V=${volt[n]}`);
}

onMounted(() => {
  ;
})

</script>

<style scoped>
.box {
  width: calc(100% - 40px);
  height: 100%;
  box-sizing: border-box;
  padding-left: 20px;
}
/* Layout */
.el-col {
  margin-bottom: 20px;
  box-sizing: border-box;
  border-radius: 8px;
}
.grid-content-wrapper {
  width: 100%;
  position: relative;
}

.chnum {
  position: absolute;
  z-index: 100;
  top: 5px;
  right: 10px;
  font-size: 16px;
  font-family: "monospace";
  font-weight: bold;
}

.grid-content {
  border-radius: 12px;
  padding: 10px;
  box-sizing: content-box;
  display: flex;
  flex-direction: column;
  background-color: var(--el-fill-color); /* #3e3e3e 暗黑模式背景色 */
  box-shadow: 5px 5px 15px rgba(239, 237, 237, 0.5),/* 外部阴影 */
   inset 1px 1px 3px rgba(255, 255, 255, 0.1);/* 内部部阴影 */
  font-family: "monospace";
  font-weight: bold;
}

.grid-content:hover{
    transform: translateY(4px);
    box-shadow: 0 2px 5px rgba(255, 255, 255, 0.5); /* 减少阴影以增强按压效果 */
}

.grid-content > div:nth-child(1){
  color: #337ab7;
}

.grid-content > div:nth-child(2){
  color: #f0ad4e;
}

.grid-content > div:nth-child(3){
  color: #d9534f;
}

/* Slider */
.slider-demo-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px;
}

:deep(.el-input-number) .el-input__inner {
  border-color: #0797f0;
}

/*::v-deep .el-input-number .el-input-group__append,
::v-deep .el-input-number .el-input-group__prepend {
  background-color: #0797f0;
}*/
</style>