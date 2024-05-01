<script setup  lang="ts">
import { CircleCloseFilled,Sunny,Moon } from '@element-plus/icons-vue'
import { ElButton } from 'element-plus'
import axios from 'axios'
import { useDark, useToggle } from "@vueuse/core";

const isDark = useDark()
const toggleDark = useToggle(isDark)

const props = defineProps(["devid",]);

async function emergencystop() {
  const res = await axios.get(`http://127.0.0.1:6661/emergencystop?devid=${props.devid}`);
}
</script>

<template>
    <div class="header-page">
        <img src="/favicon.ico">
        <h2>Q101HM Large-scale High Power Analog Driver</h2>
        <el-button type="danger" size="large" :icon="CircleCloseFilled" @click="emergencystop">EMO</el-button>
        <el-icon :size="60" @click="toggleDark()">
            <Moon v-if="isDark"/>
            <Sunny v-else />
        </el-icon>
    </div>
</template>

<style scoped>
.header-page {
    height: 120px;
    min-height: 120px;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;

    img{
        width: 60px;
    }

    h2{
        font-size: 2vw;
        margin-left: 20px;
    }

    .el-button{
        height: 60px;
        font-size: 20px;
    }

    .el-icon{

    }
}
</style>