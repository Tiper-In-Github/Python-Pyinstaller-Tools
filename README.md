[TOC]

欢迎使用Pyinstaller Tools!!
![PyinstallerTools](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/ae1c59d26bc889b5da76662422c31dec "PyinstallerTools")

项目名称：Pyinstaller Tools(python打包工具箱)
涉及语言：Python3
开源类型：19年至21年生产环境项目开源
时间节点：19年初版开发完成，21年4月首次开源
Gitee.com（https://gitee.com/wubie/Python-Pyinstaller-Tools ）
Github.com(https://github.com/Tiper-In-Github/Python-Pyinstaller-Tools )
参考及动态：CSDN：https://blog.csdn.net/qq_41501331/article/details/115799182

##### 简要描述

- Pyinstaller Tools是一款功能较为完善的Python项目打包UI，它基于Pyinstaller(如果您未安装请不要担心，客户端会自动完成最新版pyinstaller的安装)为用户提供python项目的打包服务，本质上是一个UI。但是极大便利了开发者并且提升了效率。***最初是我们团队自己运营和使用的工具，现在开源出来供初学者学习，此外，我们允许任何组织和个人，在遵守MulanPSL-2.0(木兰宽松协议)的前提下，对项目进行拷贝、下载、二次开发以及商业用途。***
- 项目仓库中是**完整的系统源码**，对于需要自用的用户，可以删除客户端中的版本检查部分代码，**程序完全可以离线运行**，联网功能仅用于我们在运营时的版本更新。

##### 通过本项目我可以学习到什么
通过本项目您可以学习到：
- Python3的基本语法
- python中socket通信
- 基于tkinter（tk）的UI界面开发布局
- 基于python语言基础，构建完整的C/S架构服务体系
- python开发基础的网络服务器(Web编程)
**PS：如果您是有python基础和开发校验的开发者，可以前往阅读Gitee仓库的Wiki（[点击前往PyinstallerToolsWiki](https://gitee.com/wubie/Python-Pyinstaller-Tools/wikis/Pyinstaller%20Tools%E6%A6%82%E8%BF%B0 "PyinstallerToolsWiki")）**

##### 项目结构

软件架构说明
.gitignore #git
README.en.md #英文文档(空)
README.md #中文文档
client #客户端
|--UppMode.py #客户端更新/修复模块
|--client.py #客户端主程序
|--config-pyinstall.ini #客户端配置文件
Server #服务端
|--Server_Main.py #服务器主程序


##### 如何部署测试？
1. 克隆下载本仓库
2.     打开项目文件夹/解压目录
3.     进入/server目录下，通过编译器或cmd启动并运行Server_Main.py，默认配置已经写入server-pyinstaller.ini中
4.     如果服务端窗口输出“监听开始..”字样，说明服务端已经开始正常工作了
5.     进入/Client目录下，用编辑器打开client(main).py文件
6.     在client(main).py文件中搜索“【这里替换为自己的IP地址或者域名】”，按代码注释的提示替换为自己的IP地址或域名(项目一直处于测试阶段，未整合为配置文件)
7.     完成修改后可以视情况看是否要修改UpMode.py，同意是替换IP地址
8.     运行client(main).py文件，除了打赏作者的图片无法加载，其他内容应该可以全部加载出来

**tip**:*不修改直接运行客户端可能会弹窗“版本检查失败”，且cmd运行不会触发main
*
![](https://img-blog.csdnimg.cn/img_convert/eedcecefe5ca037454d258aef80f0eca.png)

##### 写在最后
感谢好心人来阅读本文档，在线求个star

[![无别/Pyinstaller Tools python打包助手](https://gitee.com/wubie/Python-Pyinstaller-Tools/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/wubie/Python-Pyinstaller-Tools) 

#### 代码托管平台
[![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/152d56092e687cdfdab8855b5c6cf7fd)](http://gitee.com/)
[![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/3b5e56a9a1fa1a48a181be6de589c9ed)](http://github.com/)
