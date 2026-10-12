<template>
  <div>
    <el-container style="min-height: 100vh">
      <el-header
        style="
          display: flex;
          align-items: center;
          border-bottom: 1px solid #ddd;
          background-color: #fff;
        "
      >
        <div
          style="flex: 1; display: flex; align-items: center; font-size: 24px; font-weight: bold"
        >
          <img style="width: 40px" src="@/assets/imgs/logo.png" alt="" />
          <div style="margin-left: 5px">智能实验室预约系统</div>
        </div>
        <el-dropdown>
          <div style="display: flex; align-items: center; cursor: pointer">
            <img
              :src="userInfo?.avatar || logo"
              alt=""
              style="width: 30px; border-radius: 50%"
            />
            <div style="margin-left: 3px">{{ userInfo?.name }}</div>
          </div>
        </el-dropdown>
      </el-header>
      <el-container>
        <el-aside width="220px">
          <el-menu router style="height: 100%" default-active="/manager/home">
            <el-menu-item index="/manager/home">
              <el-icon><icon-menu /></el-icon>
              系统首页
            </el-menu-item>
            <el-menu-item index="/manager/lab">
              <el-icon><House /></el-icon>
              实验室管理
            </el-menu-item>
            <el-menu-item index="/manager/equ">
              <el-icon><Setting /></el-icon>
              设备列表管理
            </el-menu-item>
            <el-menu-item index="/manager/user">
              <el-icon><User /></el-icon>
              用户管理
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { Menu as IconMenu, House, Setting, User } from '@element-plus/icons-vue'
import { useUser } from '@/utils/user'
import logo from '@/assets/imgs/logo.png'

const { userInfo } = useUser()
</script>