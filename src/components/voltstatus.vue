<template>
  <div class="box">
    <el-row :gutter="20">
      <el-col :span="3" v-for="n in 60" :key="n">
        <div class="grid-content-wrapper">
          <div class="grid-content">
            <div>+0010.000 V</div>
            <div>+0100.000 mA</div>
            <div>+1000.000 mW</div>
            <div class="slider-demo-block">
              <el-slider v-model="value" size="small" />
              <el-input-number
                v-model="value1"
                :min="0"
                :max="100"
                size="small"
              />
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
  border-radius: 12px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #3d3c3c;
  padding: 10px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  background-color: #3e3e3e; /* 暗黑模式背景色 */
  box-shadow: 5px 5px 15px rgba(239, 237, 237, 0.5),/* 外部阴影 */
   inset 1px 1px 3px rgba(255, 255, 255, 0.1);/* 内部部阴影 */
}
.grid-content:hover{
    transform: translateY(4px);
    box-shadow: 0 2px 5px rgba(255, 255, 255, 0.5); /* 减少阴影以增强按压效果 */
}
/* Slider */
.slider-demo-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px;
}
/* input-number */
::v-deep .el-input-number .el-input__inner {
  color: #fff; /* 文字颜色 */
  background-color: rgba(255, 255, 255, 0.5); /* 背景颜色 */
  border-color: #0797f0; /* 边框颜色 */
}
::v-deep .el-input-number .el-input-group__append,
::v-deep .el-input-number .el-input-group__prepend {
  background-color: #0797f0; /* 按钮背景颜色 */
}
</style>