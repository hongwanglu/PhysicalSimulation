# 该项目主要用于AI辅助的计算物理学习及案例分享

## 使用的工具

项目采用Python语言开发，UI使用Pyside，包管理和项目管理使用的工具是uv（An extremely fast Python package and project manager, written in Rust，<https://docs.astral.sh/uv>）

## 文件目录结构

fig 用于存放图片

ui 用于存放图形界面ui文件及pyside6-uic编译生成的_ui.py文件。注意：部分_ui.py文件是直接写的，没有对应的.ui文件。

每个具体例子都对应一个或多个python文件（在工作目录下）+相应的ui目录下的ui文件。

## 使用教程

1. 克隆项目到本地 
2. 配置开发环境安装必要的软件包
3. 加入自己的代码、文档、保证代码能独立运行
4. 更新Physical_Simulation.py文件中力、热、光、电相应位置，让主程序能在相应模块中索引自己的代码

## TODO List

1. 整理文档，每个案例相关的文档/说明
2. 加入更多优秀案例
