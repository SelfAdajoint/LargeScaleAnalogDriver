<template>
  <div class="box">
    <el-row :gutter="20">
      <el-col :lg="3" :md="4" :sm="6" :xs="8" v-for="n in 64" :key="n">
        <div class="grid-content-wrapper">
          <div class="chnum">{{ n }}</div>
          <div class="grid-content">
            <div class="color1" :class="{ 'active': !isable[n] }">+ {{volt[n]}}{{ formatNumber(volt[n],8,3) }} V</div>
            <div class="color2" :class="{ 'active': !isable[n] }">+ {{ formatNumber(amp[n],8,3) }} mA</div>
            <div class="color3" :class="{ 'active': !isable[n] }">+ {{ formatNumber(volt[n]*amp[n],8,3) }} mW</div>
            <div class="slider-demo-block">
                <el-slider v-model="volt[n]" :min="0" :max="10" :step="0.01" size="small"
                  :format-tooltip="formatTooltip"
                  @change="onsliderchange(n)"
                  @input="onsliderinput(n)"
                  @mousedown="lockvolt(n)"
                  @focusout="releasevolt(n)"/>
                <el-input-number v-model="volt[n]" :min="0" :max="10" :precision="3" :step="0.001" size="small"
                  @change="setvolt(n)"/>
            </div>
            <div class="isable-box">
              <el-switch
                v-model="isable[n]"
                class="ml-2"
                width="65"
                inline-prompt
                active-text="enable"
                inactive-text="disable"
                style="--el-switch-on-color: #337ab7;"
              />
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>

import { ref, reactive, onMounted, onUnmounted, watch } from "vue";
import axios from 'axios'

function formatTooltip(number){
  return number.toFixed(3)
}

function formatNumber(num, width, precision) {
  try{
    var formatted = num.toFixed(precision);
    var padding = width - formatted.length;
    if (padding > 0) {
        formatted = '0'.repeat(padding) + formatted;
    }
    return formatted;
  }catch(error){
    console.log(`error in getvolt ${num}`,error)
  }
  return String(num)
}

const props = defineProps(["devid","isoff"]);
const volt  = reactive(Array(65).fill(0.0));
const amp   = reactive(Array(65).fill(0.0));
const isable = reactive(Array(65).fill(true));

// -------------
watch(() =>props.isoff, (newValue, oldValue) => {
  console.log(newValue, oldValue)
  isable.fill(newValue);
}, { immediate: true });

function handleisable(n){
  
}
// -------------
async function setvolt(n){
  console.log(`setvolt ${n} ${volt[n]}`)
  axios.get(`http://127.0.0.1:6661/setvolt?devid=${props.devid}&ch=${n}&V=${volt[n]}`)
  .then(res => {
    if (!res.data.success){
      // console.log(`setvolt ch $n failed`,res.data)
    }
    setTimeout(()=>{getvolt(n);}, 50)
  })
  .catch(error => {
    // console.log(`error in setvolt ${n}`,error)
  })
}

const volt_ms = reactive(Array(65).fill(0))
const volt_lock = reactive(Array(65).fill(0))

function onsliderchange(n){
  releasevolt(n)
  setvolt(n)
}

function onsliderinput(n){
  const curr_ms = new Date().getTime();
  if(curr_ms-volt_ms[n]>=100){
    volt_ms[n] = curr_ms
    setvolt(n)
  }
}

function lockvolt(n){
  console.log(`lock ${n}`)
  volt_lock[n] = 1
}

function releasevolt(n){
  console.log(`release ${n}`)
  volt_lock[n] = 0
}

async function getvolt(n){
  try{
    const res = await axios.get(`http://127.0.0.1:6661/getpowr?devid=${props.devid}&ch=${n}`)
     //console.log(res)
    if(res.data.success){
      if(volt_lock[n]==0){
        volt[n] = res.data.volt;
      }
      amp[n]  = res.data.amp;
    }else{
      // console.log(`error in getvolt ${n}`,res.data)
    }
  }catch(error){
    // console.log(`error in getvolt ${n}`,error)
  }
}

const getvoltslock = ref(0)

async function getvolts(){
  if(getvoltslock.value>0){
    console.log("another getvolts is running",getvoltslock)
    return
  }else{
    getvoltslock.value += 1
    for (var i = 1; i < volt.length; i++) {
      if(isable[i]){
        await getvolt(i);
        console.log("请求")
      }else{
        console.log("不请求")
      }
    }
    getvoltslock.value -= 1
  }
}

const timer = ref();
onMounted(() => {
  console.log("v1.5")
  getvolts()
  timer.value = setInterval(getvolts, 1000)
})
onUnmounted(() => {
  clearInterval(timer.value)
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

.color1{
  color: #337ab7;
}

.color2{
  color: #f0ad4e;
}

.color3{
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
.isable-box{
  display: flex;
  justify-content: center;
}
.active{
  color: #989595;
  /* background-color: #d9534f; */
}
</style>