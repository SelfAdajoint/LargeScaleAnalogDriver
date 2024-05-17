<script setup  lang="ts">
import { CircleCloseFilled,Sunny,Moon } from '@element-plus/icons-vue'
import { ElButton, ElNotification } from 'element-plus'
import axios from 'axios'
import { useDark, useToggle } from "@vueuse/core";
// import { provide } from 'vue'
const isDark = useDark()
const toggleDark = useToggle(isDark)
const props = defineProps(["devid",]);

// const all_disable = ref(false)
// provide('isOpen', )
const disableall = () => {
    alert(1)
}


function emergencystop() {
  axios.get(`http://127.0.0.1:6661/emergencystop?devid=${props.devid}`)
  .then(res => {
    if (!res.data.success){
        console.log('emergency stop failed',res.data);
        ElNotification({
            title: 'Emergency stop failed!',
            message: res.data.message,
            type: 'error',
        })
    }else{
        ElNotification({
            title: 'Emergency stop success.',
            type: 'success',
        })
    }
  })
  .catch(error => {
    console.error('Emergency stop error:', error);
    ElNotification({
        title: 'Emergency stop failed!',
        message: error,
        type: 'error',
    })
  })
}
</script>

<template>
    <div class="header-page">
        <img src="/favicon.ico" :class="{ 'invert': !isDark }">
        <h2>Q101HM Large-scale High Power Analog Driver</h2>
        <div>
            <el-tooltip
                class="box-item"
                effect="light"
                placement="left"
                content="Set all Volts to zero."
            >
                <el-button type="danger" size="large" :icon="CircleCloseFilled" @click="emergencystop">EMO</el-button>
            </el-tooltip>
            <el-tooltip
                class="box-item"
                effect="light"
                placement="left"
                content="Set all Volts to zero."
            >
                <el-button type="warning" size="large" :icon="CircleCloseFilled" @click="disableall">WARNING</el-button>
            </el-tooltip>
        </div>
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

    .invert {
        filter: invert(100%);
    }

    h2{
        font-size: 2vw;
        margin-left: 20px;
    }

    .el-button{
        height: 60px;
        font-size: 20px;
    }
}
</style>