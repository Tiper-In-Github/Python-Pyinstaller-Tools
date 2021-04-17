<a href='https://gitee.com/wubie/Python-Pyinstaller-Tools'><img src='https://gitee.com/wubie/Python-Pyinstaller-Tools/widgets/widget_5.svg' alt='Fork me on Gitee'></img></a>
<a align="right" href='https://gitee.com/wubie/custom-online-sign-in/stargazers'><img src='https://gitee.com/wubie/custom-online-sign-in/badge/star.svg?theme=dark' alt='star'></img></a>
# Python Pyinstaller Tools  python打包助手
<p align="center">
    <img src ="https://img.shields.io/badge/version-1.0.2-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3-blue.svg" />
</p>
<br>
<a href="http://www.tiper052.top/index.php/archives/6/">了解更多关于项目的信息？点此浏览最新官方消息【Tiper博客】</a>  

 PS:尚未完全转移到仓库，感兴趣的请耐心等待两天

#### 介绍
![avatar](http://www.tiper052.top/usr/uploads/2021/04/1797720377.jpg)
python打包助手(Python Pyinstaller Tools )，以UI界面的方式，帮助开发者快速、便捷地打包项目程序，本项目适用于几乎所有python3版本，基于Pyinstaller库进行打包，可以在大部分windows环境下实现自动安装所需依赖库.<br>
客户端程序包含了完整的<br>
1.基础打包<br>
2.进阶打包(添加软件信息)<br>
3.版本检查<br>
4.版本更新<br>
5.软件公告<br>
6.软件反馈<br>
7.软件设置<br>
8.在线打赏作者<br>
9.错误报告<br>
等功能，UI界面和交互卡顿问题可能需要有所改进，本开源项目的服务端代码整合为了一个文件，将写死的版本部分改成了读取配置文件。<br>
<h2>本项目包含完整客户端和服务端程序，客户端可离线运行</h2>
之前在火毅网络团队的时候，开发出来供内部人员使用的，所以部分弹窗和界面可能包含已过期信息和网址

####  如果该项目可以得到大家的喜欢，我会去优化和清除这些信息，并尝试改进UI和交互卡顿问题

####  由于是完整项目转移至仓库，您可以在遵守开源协议的前提下，将本项目打包发布并通过服务端维护自己的更新。是不是很棒呢

您也可以尝试将软件二次开发为单机软件，去除验证和服务器连接的部分，这样可以缩短软件加载时间

#### 软件架构
软件架构说明
.gitignore               #git
README.en.md             #英文文档
README.md                #中文文档
client                   #客户端
|--UppMode.py            #客户端更新/修复模块
|--client.py             #客户端主程序
|--config-pyinstall.ini  #客户端配置文件
Server                   #服务端
|--Server_Main.py        #服务器主程序
|--server-config.ini     #服务端配置文件

#### 如何部署测试

1.  克隆\下载本仓库
2.  打开项目文件夹/解压目录
3.  进入/server目录下，通过编译器或cmd启动并运行Server_Main.py，默认配置已经写入server-pyinstaller.ini中
4.  如果服务端窗口输出“监听开始..”字样，说明服务端已经开始正常工作了
5.  进入/Client目录下，用编辑器打开client(main).py文件
6.  在client(main).py文件中搜索“【这里替换为自己的IPIP地址或者域名】”，按代码注释的提示替换为自己的IP地址或域名(项目一直处于测试阶段，未整合为配置文件)
7.  完成修改后可以视情况看是否要修改UpMode.py，同意是替换IP地址
8.  运行client(main).py文件，除了打赏作者的图片无法加载，其他内容应该可以全部加载出来

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

