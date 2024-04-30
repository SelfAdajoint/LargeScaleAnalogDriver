<script setup  lang="ts">
import { CircleCloseFilled } from '@element-plus/icons-vue'
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
        <h2 style="font-size: 40px;">Q101HM多通道大功率模拟信号驱动器</h2>
        <el-button type="danger" size="large" :icon="CircleCloseFilled" @click="emergencystop">急&nbsp;停</el-button>
        <el-button class="border-none w-full bg-transparent cursor-pointer" @click="toggleDark()">
            <i inline-flex i="dark:ep-moon ep-sunny"/>
        </el-button>
    </div>
</template>

<style scoped>
.header-page {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    h2{
        margin-left: 20px;
    }

    .el-button{
        margin-right: 120px;
        height: 60px;
        font-size: 20px;
    }
}
</style>