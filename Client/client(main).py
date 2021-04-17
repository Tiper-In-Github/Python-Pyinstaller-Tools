#coding=utf-8
#公测版
#Software Author Informatio：  网名:无别真名:邱鹏
#错误上报使用下方代码：其中，“xy”是位置参数，写法是完整的可调用路径，cwm是错误码，识别错误用，其他参数较简单
#False_report(None,-1,title='程序出现错误了',size=(690,490),xy='Mode：LonginFrame.sz_xt',cwm='6069')
#此版本为公测版
e=0#留意
print('加载中...')   #修改协议版本号，停止对老版本的支持
global ver
ver = 'V1.0.2'
import wx
import telnetlib #用于FPA协议通讯
from time import sleep
import _thread as thread
from PIL import ImageGrab   #用于实现全屏截屏
import time
import os
import gc
import stat
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import subprocess
import configparser
from IPy import IP
import socket
import random
import platform
import winsound
import uuid
import struct
import urllib.request
import sys
import psutil
from tkinter import filedialog
import tkinter
#import win32com.client  #需要下载pywin32
#import cv2
#speaker = win32com.client.Dispatch("SAPI.SpVoice")
#为确保迁移性，系统生成数据路径使用绝对路径C:/FPA_OS/！！！！！！！！！或自定义

#通信协议版本
global communication_protocol
communication_protocol = 'HV.1.0.0'
#程序记录版本
global Program_version
Program_version = 'FPA聊天系统V1.1.0(公测版)请留言服务器公告是否有更新通知'
veri = 'HV1.0.0'
servername='logo'
if os.path.isfile("upde.bat"):  #如果有更新脚本存在，按理来讲应该新程序可以运行到时候删除
    os.remove("upde.bat")
    print('[恭喜]感谢！您完成了软件升级，您正在体验%s版本!' %veri)


class LOG_OS():  #文件系统//基础系统//首次运行及账户安全系统

    def log_log(self,event):  #运行日志
        try:
            LOG_FILE = open('C:/FPA_OS/log/log_file_pyinstall.txt', 'a+')
            LOG_OS.try_Size(LOG_OS, 1)
        except:
            print('文件夹缺失，正在修复...')
            print('[首次运行]创建环境')
            try:
                os.makedirs('C:/FPA_OS/log')
            except:
                pass
            try:
                os.makedirs('C:/FPA_OS/Chat/')
            except:
                pass
            try:
                os.makedirs('C:/FPA_OS/folder/')
            except:
                pass
            try:
                os.makedirs('C:/FPA_OS/截屏目录')
            except:
                pass
            print('修复完成')
            print("你好，欢迎使用聊天室\n软件没有在该计算机发现任何聊天室遗留文件及记录，\n属于首次运行。现在程序已经准备就绪了，请重启软件。\n\n10秒后自动退出\n联盟官方网站及官方下载www.huoyinetwork.cn")
            time.sleep(10)
            LOG_FILE = open('C:/FPA_OS/log/log_file_user.txt', 'a+')
            t = time.strftime('%F %H:%M:%S')
            LOG_FILE.write('[%s][文件系统][首次运行]新建程序专用文件夹（<C:/FPA_OS><C:/FPA_OS/log><C:/FPA_OS/Chat><C:/FPA_OS/folder><C:/FPA_OS/截屏目录>）\n' %t)
            LOG_FILE.write('[首次运行]程序路径：%s\n' %os.getcwd())

            LOG_FILE.close()
        f = str(event)
        t = time.strftime('%F %H:%M:%S')
        text = ('[:%s]Event:%s \n' % (t, f))
        LOG_FILE.write(text)
        LOG_FILE.close()
        pass

    def log_del(self):  # 清理缓存（log，截图）
        LOG_OS.log_log(LOG_OS, '文件系统[清理缓存]')
        print('[文件系统]清理缓存')
        try:
            # del(Program_version)
            os.remove('C:\FPA_OS\log\log_file_user.txt')
            os.chmod('C:\FPA_OS\log\log_file_user.txt', stat.S_IWRITE)  # 删除对应版本日志文件
            # os.chmod('E:\FPA_OS\截屏目录', stat.S_IWRITE)
        except:
            print('未知[判断错误请忽略]：已经执行完了清理，但是不确定是否完全删除')
            LOG_OS.log_log(LOG_OS, '文件系统[未知：已经执行完了清理，但是不确定是否完全删除]')
        else:
            print('成功:日志缓存清理完成！')
            LOG_OS.log_log(LOG_OS, '文件系统[清理日志缓存完成]')
            try:
                os.chmod('C:\FPA_OS\截屏目录', stat.S_IWRITE)
            except:
                print('失败：无法删除截屏缓存文件！')
                LOG_OS.log_log(LOG_OS, '文件系统[清理截屏缓存失败]')
            else:
                print('成功:删除截屏缓存成功')
            print('清理完成')

    def try_Size(self,e):
        log_size = os.path.getsize('C:/FPA_OS/log/log_file_user.txt')  # 获取日志大小
        #print(log_size)
        if log_size >= 104857600:  #字节大小
            print('日志缓存占用过大（大于100MB）请及时清理缓存')
            #winsound.Beep(900, 2000)
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)   #winsound.SND_ASYNC可以让声音播放的时候程序继续运行
            # 其中600表示声音大小，1000表示发生时长，1000为1秒
        #self.getFileSize(path='C:/FPA_OS/截屏目录')  # 获取截屏缓存大小
        #print(self.getFileSize(self,filePath="C:/FPA_OS/截屏目录"))
        jiep_size = self.getFileSize(self,filePath="C:/FPA_OS/截屏目录")  #获取文件夹大小
        if jiep_size >= 901775360:  #字节大小
            print('截屏缓存占用过大（大于860MB），虽然不影响软件运行，但是建议清理')
            dlg = wx.MessageDialog(self,"提醒：\n检测到截屏缓存占用过大（大于860MB）\n虽然不影响软件运行，但是建议清理\n在操作菜单选择“删除截屏”或手动到'E:\FPA_OS\截屏目录'目录下删除文件","清理提醒")
            dlg.ShowModal()
            # self.control.SelectAll();
            dlg.Destroy()

    def getFileSize(self,filePath, size=0):  #获取文件夹大小
        for root, dirs, files in os.walk(filePath):
            for f in files:
                size += os.path.getsize(os.path.join(root, f))
                #print(f)  #输出文件名
        return size

    def get_mac():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    def pyinstalllog(self,pd,text):
        file = open('%s\instlog.txt' % pd, 'a')
        file.write('%s\n' % text)
        file.close()


class False_report(wx.Frame):    #错误上报
    def __init__(self, parent, id, title, size,xy,cwm,fwqk):
        global my_sender
        global my_pass
        global weiz
        global cwms
        global fw
        fw = fwqk
        self.TestPlatform(e=0)
        cwms=cwm
        osnn=('\n%s' %osn)
        self.weiz = xy
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.icon = wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO)
        self.SetSize(size)
        self.SetIcon(self.icon)
        self.Center()
        wx.StaticText(self, label="程序出现了一些错误，对此我表示非常抱歉，请利用半分钟的时间。", pos=(10, 0), size=(300, 20))
        wx.StaticText(self, label="向我描述一下错误出现的情况(操作系统的类型、网络状态、什么时候出现的)", pos=(10, 20), size=(180, 30))
        ti=report_time=time.strftime('%F %H:%M:%S')
        wx.StaticText(self, label="报告文档将包含以下信息:\n操作系统的类型:%s\n日志记录\n软件及协议版本\n出现错误的模块\n用户描述\n时间\n以上信息不包含你的任何隐私\n及可以定位到你的信息请放心发送\n\n系统记录的相关数据\n错误码：%s\n问题模块:%s\n时间:%s\n访问情况:%s\n" %(osnn,cwm,xy,ti,fwqk), pos=(380, 30), size=(220,430))
        self.yhmsLabel = wx.StaticText(self, label="问题描述", pos=(40, 100), size=(120, 25))
        scname = "请描述你出现此问题当时的情况（如：在进行什么操作或查看什么的时候）,如果可以，请留下联系方式。"
        self.yhms = wx.TextCtrl(self, value=scname, pos=(10, 37), size=(350, 295))

        self.portButton = wx.Button(self, label='发送', pos=(20,345), size=(300, 30))

        self.portButton.Bind(wx.EVT_BUTTON, self.report)

        LOG_OS.log_log(LOG_OS, '加载程序[错误报告窗口完成]')
        self.Show()

    def TestPlatform(self,e):
        #操作系统的类型
        #print("----------Operation System--------------------------")
        # Windows will be : (32bit, WindowsPE)
        # Linux will be : (32bit, ELF)
        #print(platform.architecture())
        osy=platform.architecture()
        osx=platform.platform()
        global osn
        osn= ('%s-/-%s' %(osy,osx))

        # Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
        # Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-Final
        #print(platform.platform())

        # Windows will be : Windows
        # Linux will be : Linux
        #print(platform.system())
        #python版本
        #print("--------------Python Version-------------------------")
        # Windows and Linux will be : 3.1.1 or 3.1.3
        #print(platform.python_version())


    def FalseDialog(self,title, content, size):
        # 显示信息对话框
        winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
        LOG_OS.log_log(LOG_OS, '[错误上报模块]%s' % content)
        dialog = wx.Dialog(title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label='错误上报模块')
        wx.StaticText(dialog, label=content)
        dialog.ShowModal()

    def report(self,e):
        print('准备数据中...')
        LOG_OS.log_log(LOG_OS,'[错误上报]为错误上报准备数据中')
        #数据准备区
        my_sender = '2048408982@qq.com'  # 发件人邮箱账号
        #my_pass = 'yirhscprfufbebgj'  # 发件人邮箱密码(当时申请smtp给的口令)
        vic='V1.1.0(公测版)'#软件版本
        vtc='FPA1.0.2'#协议版本
        NOW_path = os.getcwd()  #安装路径
        report_time=time.strftime('%F %H:%M:%S')  #上报时间
        report_weiz=self.weiz  #出现错误的代码位置（记得更新）
        try:
            report_user=username  #用户昵称
            LOG_OS.log_log(LOG_OS, '[错误上报]昵称:%s' %username)
        except:
            report_user='未登录'  #用户昵称
            LOG_OS.log_log(LOG_OS, '[错误上报]用户未登录')
        yhms=self.yhms.GetLineText(0)  #用户描述
        report_cwm=cwms

        if yhms == '':
            report_yhms='用户没有对此问题进行描述'
            LOG_OS.log_log(LOG_OS, '[错误上报]用户没有对此问题进行描述')
        else:
            report_yhms=yhms  #用户描述
        mac =LOG_OS.get_mac()
        log=open('C:/FPA_OS/log/log_file_user.txt', 'r+')
        report_dlog=log.read()
        log.close()

        my_user = '2048408982@qq.com'  # 收件人邮箱账号，测试邮箱（詹）2743157437@qq.com
        to_name = '来自软件：FPA聊天网络'
        zhuti = ('错误上报程序报告')
        text = ('''
    =====错误报告====
    [操作系统信息:%s;设备MAC地址:%s]
    [客户端版本:%s;协议:%s]
    [时间:%s;位置:%s;用户昵称:%s]错误码：%s]
    [Path:%s]
    <访问情况:%s>
    系统日志------
    %s

    用户描述： %s
        ''' %(osn,mac,vic,vtc,report_time,report_weiz,report_user,report_cwm,NOW_path,fw,report_dlog,report_yhms))
        # 数据准备区结束
        LOG_OS.log_log(LOG_OS, '[错误上报]准备完成')
        #ret = True
        LOG_OS.log_log(LOG_OS, '[错误上报]数据载入完成')
        try:
            msg = MIMEText(text, 'plain', 'utf-8')
            msg['From'] = formataddr(["错误上报程序",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号(！一般固定！)
            msg['To'] = formataddr([to_name, my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = zhuti  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(my_sender,'zahqizjfrhpacaic')  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            LOG_OS.log_log(LOG_OS, '[错误上报]发送报告')
            server.quit()  # 关闭连接
            LOG_OS.log_log(LOG_OS, '[错误上报]关闭连接')
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            #ret = False
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            t = time.strftime('%H:%M:%S')
            print("报告发送失败 TIME:%s" % t)
            LOG_OS.log_log(LOG_OS, '[错误上报]报告发送失败 TIME:%s' % t)
            title = '报告发送失败'
            content = '抱歉，报告发送失败\n你可以添加作者qq反馈。'
            size = (200, 100)
            LOG_OS.log_log(LOG_OS, '[错误上报]%s' % content)
            dialog = wx.Dialog(self,title=title, size=size)
            dialog.Center()
            wx.StaticText(dialog, label='错误上报模块')
            wx.StaticText(dialog, label=content)
            dialog.ShowModal()
        else:
            t = time.strftime('%H:%M:%S')
            print("报告发送成功 TIME:%s" % t)
            LOG_OS.log_log(LOG_OS, '[错误上报]报告发送成功 TIME:%s' % t)
            title = '报告发送成功'
            content = '感谢你对我的支持\n我会尽快找到问题原因,软件会退出。'
            size = (200, 100)
            LOG_OS.log_log(LOG_OS, '[错误上报]%s' % content)
            dialog = wx.Dialog(self,title=title,size=size)
            dialog.Center()
            wx.StaticText(dialog, label='错误上报模块')
            wx.StaticText(dialog, label=content)
            dialog.ShowModal()
            print('关闭后3秒退出程序..')
            LOG_OS.log_log(LOG_OS,'[发生错误]上报完成，即将关闭窗口并退出')
            time.sleep(3)
            self.Close() #关闭窗口
            exit()

        #return ret
    #ret = report()
    #ret=report()
class shezhi(wx.Frame): #软件设置
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.icon = wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.SetSize(690, 490)
        self.Center()

        mianban = self.read()
        #self.shezhi = mianban[2]

        wx.StaticText(self, label="主界面背景色", pos=(10, 20))
        list1 = ['默认', '黑色','白色']
        self.beij = wx.ComboBox(self, -1, value=mianban[0], choices=list1, style=wx.CB_SORT, pos=(10, 40))
        wx.StaticText(self, label="主界面字体色", pos=(10, 80))
        list1 = ['默认', '黑色','白色']
        self.zti = wx.ComboBox(self, -1, value=mianban[1], choices=list1, style=wx.CB_SORT, pos=(10, 100))
        wx.StaticText(self, label="日志存放于", pos=(10, 140))
        self.aspath = wx.TextCtrl(self, pos=(85, 140), size=(300, 25), style=wx.TE_PROCESS_ENTER)  # 输入框
        self.openfileButton = wx.Button(self, label="浏览", pos=(390, 140), size=(140, 25))
        self.openfileButton.Bind(wx.EVT_BUTTON, self.OpenFile)
        self.aspath.write(mianban[2])
        wx.StaticText(self, label="为方便检查错误，本软件支持将日志以中文内容形式保存于txt文件中。", pos=(10, 170))
        wx.StaticText(self, label="设置更新时间：%s" %mianban[3], pos=(10, 200))


        self.serverButton = wx.Button(self, label='保存设置', pos=(20, 345), size=(300, 30))
        self.serverButton.Bind(wx.EVT_BUTTON, self.server)
        self.Show()

    def read(self):
        config = configparser.ConfigParser()
        re = config.read('config-pyinatll.ini')
        if os.path.isfile('config-pyinatll.ini'):
            #global background
            background = config.get('mianban', option='background')#背景颜色
            Typeface = config.get('mianban', option='typeface')#字体颜色
            logpath = config.get('mianban',option='logpath')
            newtime = config.get('time',option='newtime')
            return background, Typeface, logpath, newtime
        else:
            background = '默认系统'
            Typeface = '默认系统'
            logpath = 'C:\FPA_OS\log\log_file_pyinstall.txt'
            newtime = '您还未更新过设置'
            return background, Typeface, logpath, newtime

    def server(self,e):
        background = self.beij.GetStringSelection()
        Typeface = self.zti.GetStringSelection()
        logpaths = self.aspath.GetStringSelection()
        newtime = time.strftime('%F %H:%M:%S')
        print('data',background,'\n',Typeface)
        config = configparser.ConfigParser()
        # set a number of parameters
        config.add_section("mianban")  # 设置数据主体部分
        config.set("mianban", "background", background)  # 背景颜色设置
        config.set("mianban", "Typeface", Typeface)  # 字体颜色设置
        config.set("mianban", "logpath", logpaths)  # 日志设置
        config.add_section("time")
        config.set("time", "newtime", newtime)
        # write to file
        config.write(open('config-pyinatll.ini', "w"))

    def xiugai(self,e):
        # 修改：
        # !/usr/bin/env python
        # -*- coding: utf-8 -*-
        #import ConfigParser
        config = configparser.ConfigParser()
        config.read('1.ini')
        a = config.add_section("md5")
        config.set("md5", "value", "1234")
        config.write(open('1.ini', "r+"))  # 可以把r+改成其他方式，看看结果:)

    def OpenFile(self, event):
        '''
        打开开文件对话框（浏览文件）
        '''
        file_wildcard = "文本文件(*.txt)|*.txt|日志文件(*.log)|*.log|所有文件(*.*)|*.*"
        dlg = wx.FileDialog(self, "指定日志记录文件（txt/log）",
                            os.getcwd(),
                            style=wx.OS_UNIX_OPENBSD,
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()  # 获取文件路径
            print('path:', self.filename)  # 打印路径
            self.aspath.write(self.filename)  # 将路径发送到输入框
            #self.ReadFile()
            self.SetTitle(self.title + '--' + self.filename)

        dlg.Destroy()


class giteeapishezhi(wx.Frame): #码云配置
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.icon = wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.SetSize(690, 490)
        self.Center()

        wx.StaticText(self, label="仓库完整地址", pos=(10, 25))
        self.pathy = wx.TextCtrl(self, pos=(85, 25), size=(300, 25), style=wx.TE_PROCESS_ENTER)  # 输入框
        self.closeButton = wx.Button(self, label="没有仓库？创建一个！", pos=(390, 25), size=(140, 25))
        wx.StaticText(self, label="私人令牌/授权码", pos=(10, 60))
        self.pathy = wx.TextCtrl(self, pos=(85, 60), size=(300, 25), style=wx.TE_PROCESS_ENTER)  # 输入框
        self.closeButton = wx.Button(self, label="忘记私人令牌", pos=(390, 60), size=(140, 25))
        wx.StaticText(self, label="仓库所属空间", pos=(10, 100))
        self.pathy = wx.TextCtrl(self, pos=(85, 100), size=(300, 25), style=wx.TE_PROCESS_ENTER)  # 输入框
        #self.closeButton = wx.Button(self, label="忘记私人令牌", pos=(390, 60), size=(140, 25))
        wx.StaticText(self, label="文件路径", pos=(10, 140))
        self.filepath = wx.TextCtrl(self, pos=(85, 140), size=(300, 25), style=wx.TE_PROCESS_ENTER)  # 输入框
        self.openfileButton = wx.Button(self, label="浏览", pos=(390, 140), size=(140, 25))
        self.openfileButton.Bind(wx.EVT_BUTTON,self.OnOpen)

        self.Show()

    def OnOpen(self, event):
        '''
        打开开文件对话框（浏览文件）
        '''
        file_wildcard = "项目描述文件(*.md)|*.md|压缩文件(*.rar)|*.rar|压缩文件(*.zip)|*.zip|文本文件(*.txt)|*.txt|所有文件(*.*)|*.*"
        dlg = wx.FileDialog(self, "选择项目文件",
                            os.getcwd(),
                            style=wx.OS_UNIX_OPENBSD,
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()#获取文件路径
            print('path:',self.filename)#打印路径
            self.filepath.write(self.filename)#将路径发送到输入框
            #self.ReadFile()
            self.SetTitle(self.title + '--' + self.filename)

        dlg.Destroy()

class False_fankui(wx.Frame):    #软件反馈
    def __init__(self, parent, id, title):
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.icon = wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.SetSize(690,490)
        self.Center()
        wx.StaticText(self, label="你的意见将使我们把软件做得更好.", pos=(10, 0), size=(300, 20))
        wx.StaticText(self, label="向我们反馈你遇到的问题及你的建议", pos=(10, 20), size=(180, 30))
        ti=time.strftime('%F %H:%M:%S')
        wx.StaticText(self, label="报告文档将不会包含除时间及你稍后填写的内容外的其他任何信息\n如果可以，请在描述完后留下联系方式（微信、QQ、电话、邮箱），作者会在48小时（一般12小时）内回复你。\nTime:%s" %ti , pos=(400, 30), size=(220,330))
        self.yhmsLabel = wx.StaticText(self, label="你的遇到了什么问题或不方便？又或者希望软件在哪方面进行改进？", pos=(40, 100), size=(120, 25))
        scname = "反馈内容"
        self.yhms = wx.TextCtrl(self, value=scname, pos=(10, 37), size=(379, 295))

        self.portButton = wx.Button(self, label='反   馈', pos=(20,345), size=(379, 30))

        self.portButton.Bind(wx.EVT_BUTTON, self.report)

        LOG_OS.log_log(LOG_OS, '反馈程序[反馈窗口完成]')
        self.Show()

    def FalseDialog(self,title, content, size):
        # 显示信息对话框
        LOG_OS.log_log(LOG_OS, '[用户反馈模块]%s' % content)
        dialog = wx.Dialog(title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label='用户反馈模块')
        wx.StaticText(dialog, label=content)
        dialog.ShowModal()

    def report(self,e):
        print('准备数据中...')
        LOG_OS.log_log(LOG_OS,'[用户反馈]为错误上报准备数据中')
        #数据准备区
        my_sender = '2048408982@qq.com'  # 发件人邮箱账号
        report_time=time.strftime('%F %H:%M:%S')  #上报时间
        try:
            report_user=username  #用户昵称
            LOG_OS.log_log(LOG_OS, '[用户反馈]昵称:%s' %username)
        except:
            report_user='未登录'  #用户昵称
            LOG_OS.log_log(LOG_OS, '[用户反馈]用户未登录')
        yhms=self.yhms.GetLineText(0)  #用户描述


        if yhms == '':
            report_yhms='用户没有对此问题进行描述'
            LOG_OS.log_log(LOG_OS, '[用户反馈]用户没有对此问题进行描述')
        else:
            report_yhms=yhms  #用户描述

        my_user = '2048408982@qq.com'  # 收件人邮箱账号，测试邮箱（詹）2743157437@qq.com
        to_name = '来自软件：FPA聊天网络'
        zhuti = ('用户反馈程序报告')
        text = ('''
    =====用户反馈====
一个用户向你发送了反馈
    [时间:%s用户昵称:%s]

    用户反馈的内容------
    %s

        ''' %(report_time,report_user,report_yhms))
        # 数据准备区结束
        LOG_OS.log_log(LOG_OS, '[用户反馈]准备完成')
        #ret = True
        LOG_OS.log_log(LOG_OS, '[用户反馈]数据载入完成')
        try:
            msg = MIMEText(text, 'plain', 'utf-8')
            msg['From'] = formataddr(["用户反馈程序",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号(！一般固定！)
            msg['To'] = formataddr([to_name, my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = zhuti  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(my_sender,'zahqizjfrhpacaic')  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            LOG_OS.log_log(LOG_OS, '[用户反馈]发送报告')
            server.quit()  # 关闭连接
            LOG_OS.log_log(LOG_OS, '[用户反馈]关闭连接')
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            #ret = False
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            t = time.strftime('%H:%M:%S')
            print("反馈信息发送失败 TIME:%s" % t)
            LOG_OS.log_log(LOG_OS, '[用户反馈]反馈信息发送失败 TIME:%s' % t)
            title = '反馈信息发送失败'
            content = '抱歉，反馈信息发送失败\n你可以添加作者qq反馈。'
            size = (200, 100)
            LOG_OS.log_log(LOG_OS, '[用户反馈]%s' % content)
            dialog = wx.Dialog(self,title=title, size=size)
            dialog.Center()
            wx.StaticText(dialog, label='用户反馈模块')
            wx.StaticText(dialog, label=content)
            dialog.ShowModal()
        else:
            t = time.strftime('%H:%M:%S')
            print("报告发送成功 TIME:%s" % t)
            LOG_OS.log_log(LOG_OS, '[用户反馈]报告发送成功 TIME:%s' % t)
            title = '报告发送成功'
            content = '感谢你对我的支持\n我会尽快处理。'
            size = (200, 100)
            LOG_OS.log_log(LOG_OS, '[用户反馈]%s' % content)
            dialog = wx.Dialog(self,title=title,size=size)
            dialog.Center()
            wx.StaticText(dialog, label='用户反馈模块')
            wx.StaticText(dialog, label=content)
            dialog.ShowModal()
            LOG_OS.log_log(LOG_OS,'[用户反馈]上报完成，即将关闭窗口并退出')
            time.sleep(3)
            self.Close() #关闭窗口




def ChatDialog(title, content, size):
    # 显示错误信息对话框
    LOG_OS.log_log(LOG_OS, '[聊天记录模块]%s' % content)
    dialog = wx.Dialog(title=title, size=size)
    dialog.Center()
    wx.StaticText(dialog, label='记录模块')
    wx.StaticText(dialog, label=content)
    dialog.ShowModal()


LOG_OS.log_log(LOG_OS, '加载程序[整体模块]')


class LoginFrame(wx.Frame):
    """
    登录窗口
    """
    def __init__(self, parent, id, title, size):
        
        LOG_OS.log_log(LOG_OS, '加载程序[初始化登陆窗口，绑定按钮]')
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.icon = wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.SetSize(size)
        self.Center()

        # 下载在线图片
        try:
            d = os.getcwd()  # 当前路径
            urllib.request.urlretrieve('http://www.huoyinetwork.cn/static/HO/home.png', "%s\\home.png" % d)
        except:
            print('获取最新首页图片失败，请检查网络。')
        try:
            d = os.getcwd()  # 当前路径
            urllib.request.urlretrieve('http://www.huoyinetwork.cn/static/HO/login.png', "%s\\login.png" % d)
        except:
            print('获取最新登陆图片失败，请检查网络。')

        # panel = wx.Panel(window)
        # 利用wxpython的GridBagSizer()进行页面布局
        sizer = wx.GridBagSizer(0, 2)  # 列间隔为10，行间隔为20
        # 添加北京字段，并加入页面布局，为第二行，第一列

        # 获取beijing.png图片，转化为Bitmap形式，添加到第二行，第二列
        image2 = wx.Image('login.png', wx.BITMAP_TYPE_PNG).Rescale(320, 390).ConvertToBitmap()
        bmp2 = wx.StaticBitmap(self, -1, image2)  # 转化为wx.StaticBitmap()形式
        sizer.Add(bmp2, pos=(0, 32), flag=wx.ALL, border=5)
        # 将Panmel适应GridBagSizer()放置
        self.SetSizerAndFit(sizer)

        #image_file = 'dl.jpg'  # 添加背景,由于添加背景了，所以要在下面的部分wx代码里要在self后面添加.bitmap
        #to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))

        wx.StaticText(self, label="*使用指南: 输入服务器名称索引（主服：FPA），设置好自己的昵称，点击登陆即刻进入接待大厅。", pos=(10, 0), size=(370, 40))
        wx.StaticText(self, label="*产品内测及交流群：742761151\n觉得软件好用欢迎赞助作者*为了你的安全，请勿使用IP直接连接。", pos=(10, 40), size=(300, 50))
        #wx.StaticText(self.bitmap, label="背景图片在软件文件夹，名字“dl”可替换，不可删除", pos=(10, 250), size=(300, 20))
        self.serverAddressLabel = wx.StaticText(self, label="服务器", pos=(40, 120), size=(120, 25))
        self.userNameLabel = wx.StaticText(self, label="昵称", pos=(40, 150), size=(120, 25))

        try:
            print('***********')
            config = configparser.ConfigParser()
            re=config.read('config-sr.ini')
            #print(re)
            # return config.get('ftpd-sr', v)
            global ID
            if os.path.isfile('config-sr.ini'):
                #passtext.SetEditable(1)
                global scname
                global server
                global ids
                scname=config.get('fpa(CN)-sr',option='username')
                server=config.get('fpa(CN)-sr',option='server')
                ids=config.get('fpa(CN)-sr',option='userid')#身份编号可以用来拓展出会员功能、禁言等功能
                print(scname)
                # name=open('C:/FPA_OS/folder/name.txt','r')
                # scname=str(name.read())
                LOG_OS.log_log(LOG_OS, '从配置文件恢复用户昵称:%s' % scname)
                LOG_OS.log_log(LOG_OS, '从配置文件恢复登陆服务器:%s' % server)
                LOG_OS.log_log(LOG_OS, '从配置文件恢复身份编号:%s' % ids)
                # name.close()
            else:
                LOG_OS.log_log(LOG_OS, '第一次使用，无身份编号')
                ids=''

            if scname == '' or server == '':
                server='请输入服务器索引'
                scname="第一次使用，请设置昵称"
                LOG_OS.log_log(LOG_OS, '用户第一次使用')

        except:
            server = '请输入服务器索引'
            scname = "第一次使用，请设置昵称"
            ids = ''
            LOG_OS.log_log(LOG_OS, '用户第一次使用')

        self.serverAddress = wx.TextCtrl(self,value=server,pos=(120, 120), size=(150, 25))
        self.userName = wx.TextCtrl(self,value=scname,pos=(120,150), size=(150, 25))

        self.loginButton = wx.Button(self, label='登    陆', pos=(80, 200), size=(140, 30))
        self.LOdelButton = wx.Button(self,label='清理缓存',pos=(80,360),size=(60,30))
        self.UprjButton = wx.Button(self,label='更新软件',pos=(150,360),size=(60,30))
        #self.LOsezButton = wx.Button(self,label='设置频率',pos=(150,185),size=(60,50))
        self.quitsButton = wx.Button(self,label='退 出',pos=(270,360),size=(50,24))

        #self.LOsezButton.Bind(wx.EVT_BUTTON,self.sz_xt)
        self.quitsButton.Bind(wx.EVT_BUTTON,self.quit)
        self.UprjButton.Bind(wx.EVT_BUTTON,self.Vicx)
        # 绑定登录方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        global serverAddress
        serverAddress = self.serverAddress
        #清理缓存
        self.LOdelButton.Bind(wx.EVT_BUTTON,LOG_OS.log_del)
        LOG_OS.log_log(LOG_OS, '加载程序[登陆窗口完成]')
        self.ver_jc()
        self.Show()

    def Vicx(self, e):
        print('启动更新模块...')  # 更新程序将下载对应操作系统的软件压缩包（64/32）并以覆盖的方式解压到当前文件夹
        LOG_OS.log_log(LOG_OS, '[用户执行]更新客户端')
        time.sleep(1)
        dlg = wx.MessageDialog(self,
                               "本客户端版本：V1.1.0\n通讯协议: FPA1.0.2-\n程序将会连接版本服务器获取最新版本程序更新\n并自动覆盖当前软件（如果是最新版则修复客户端）\n点击ok开始",
                               "软件更新程序", wx.OK)
        dlg.ShowModal()
        # self.control.SelectAll();
        dlg.Destroy()

        try:
            LOG_OS.log_log(LOG_OS, '用户开启更新程序')
            # os.system('Help.exe')
            global mProcess
            LOG_OS.log_log(LOG_OS, '[更新模块]启动新进程进行更新')
            #os.system('python -m UpMode.py')
            os.system('UpMode.exe')
            # mProcess = subprocess.Popen('UpMode.py', stdout=subprocess.PIPE,stderr=subprocess.PIPE)  # 官方推荐用此模块代替os.system方法---创建一个进程运行目标程序()其中PIPE指创建一个管道
            # print(returnCode)
        except:
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            print('FileError:抱歉，我们没有找到升级程序，请确认软件包是否有丢包或被修改')
            LOG_OS.log_log(LOG_OS, '[FileError]抱歉，没有找到帮助程序，请确认软件包是否有丢包或被修改')
            dlg = wx.MessageDialog(self, "FileError:抱歉，我们没有找到帮助程序，请确认软件包是否有丢包或被修改", "[更新模块不存在]", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

    def Version_checking(self):  # 版本检查
        print('[%s][自动检查版本]连接版本服务器..\n' % (time.strftime("%F %H:%M:%S")))
        LOG_OS.log_log(LOG_OS,'[自动检查版本]连接版本服务器..')
        try:
            client = socket.socket()  # 生成socket连接对象
            ip_port = ("106.12.103.112", 6979)  # 地址和端口号 填localhost可以进行本地测试【这里替换为自己的IP地址或者域名】
            client.connect(ip_port)  # 连接
        except:
            print("[%s]状态：连接服务器失败！" % (time.strftime("%F %H:%M:%S")))
            LOG_OS.log_log(LOG_OS, '[自动检查版本]连接服务器失败！')
            dlg = wx.MessageDialog(self, "Error:抱歉，检查更新失败，我们无法连接至版本服务器", "[版本服务器连接失败]", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return
            #time.sleep(3)
            #exit()
        else:
            print("[%s]状态：服务器连接没有出错" % (time.strftime("%F %H:%M:%S")))
            LOG_OS.log_log(LOG_OS, '[自动检查版本]服务器连接没有出错')
        bit = struct.calcsize("P") * 8
        content = ("Verg 1215")
        client.send(content.encode("utf-8"))  # 传送和接收都是bytes类型
        time.sleep(1)
        # 1.先接收长度，建议8192
        server_response = client.recv(1024)
        new_ver, gx_log, gx_nei = str(server_response).split('@')
        # new_ver = str(server_response.decode("utf-8"))
        client.close()
        return new_ver, gx_log, gx_nei

    def ver_jc(self):
        LOG_OS.log_log(LOG_OS, '[自动检查版本]开始检查版本...')
        global ver_nei
        try:
            ver_news, ver_log, ver_ei = self.Version_checking()
            ver_nei = (ver_ei[:-1])  # 去除最后面的英文逗号'得到正确的后缀名
            if ver_news != "b'%s" % veri:
                LOG_OS.log_log(LOG_OS, '[自动检查版本]发现新版本.%s' %ver_news)
                dlg = wx.MessageDialog(self, '有可用更新！！\n最新版本：%s\n新版本简介：%s\n-*-请点击登陆界面下方的更新按钮完成更新！\n' % (ver_news, ver_log), "更新提醒", wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
            print(ver_news)
            print(ver_log)
        except:
            print('error:版本检查失败')


    def sz_xt(self,e):  # 默认隐藏的频率设置
        try:
            wx.StaticText(self,label='数据刷新频率（建议0.1-1）',pos=(80, 220), size=(150, 25))
            slider = wx.TextCtrl(self,value='',pos=(80, 240), size=(150, 25))
            global times
            times = slider.GetLineText(0)
            if times > 1.0:
                winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
                print('参数错误:刷新频率被设置大于1秒')
                LOG_OS.log_log(LOG_OS,'[刷新频率]参数错误:刷新频率被设置大于1秒')
                self.showDialog('参数错误','刷新频率被设置大于1秒\n已经默认设置为0.4，稍后可以再做调整')
                times = 0.4
            else:
                LOG_OS.log_log(LOG_OS,'[刷新频率]用户设置:刷新频率被设置为%s秒' %times)
        except:
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            times = 0.4
            LOG_OS.log_log(LOG_OS,'[刷新频率]用户设置时出现错误，将默认为%s' %times)
            self.sorry()

    def sorry(self):
        winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
        LOG_OS.log_log(LOG_OS, '错误[%s]' % '调制器错误：6069')
        dialog = wx.Dialog(self,title='系统设置错误', size=(200,100))
        dialog.Center()
        wx.StaticText(dialog, label='错误')
        wx.StaticText(dialog, label='调制器错误：6069\n请向我们反馈')
        dialog.ShowModal()
        False_report(None,-1,title='程序出现错误了',size=(690,490),xy='Mode：LonginFrame.sz_xt',cwm='6069',fwqk='未连接任何聊天室')


    def login(self, e):
        # 登录处理
        global times
        try:  #如果没有设置就默认0.4
            ss=times
            LOG_OS.log_log(LOG_OS,'[登陆处理]设置模块设置（不肯定是用户设置）刷新频率%s' %ss)
        except:
            times=0.4
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            LOG_OS.log_log(LOG_OS, '[登陆处理]设置默认刷新频率%s' % times)
        #try:
            #name = open('C:/FPA_OS/folder/name.txt','w')#覆盖
            #text=str(self.userName.GetLineText(0))  #注意！是GetLineText(0)
            #print('name:' + text)
            #sname=text.encode('utf-8')
            #sname=text
            #name.write('%s' %sname)
            #name.close()
        #except:
        #    LOG_OS.log_log(LOG_OS,'保存昵称的时候出现错误，可能缺失[folder]')
        #    try:
        #        #如果没有记录几乎属于第一次
        #        os.makedirs('C:/FPA_OS/folder/')
        #    except:
        #        LOG_OS.log_log(LOG_OS, '[首次运行]创建文件的时候出现错误，其他错误')
        #    else:
        #        LOG_OS.log_log(LOG_OS, '[首次运行遗漏文件夹]文件夹补齐[folder]')
        #        name = open('C:/FPA_OS/folder/name.txt', 'w+')  # 覆盖
        #        text = self.userName.GetLineText(0)
        #        sname = text.encode('utf-8')
        #        name.write('%s' % sname)
        #        name.close()
        LOG_OS.log_log(LOG_OS, '处理事件[登陆]')
        #try:
        serverAddress = self.serverAddress.GetLineText(0).split(':')
        global userinname
        userinname = str(serverAddress)
        #self.serverAddress.Clear()  #删除索引
        LOG_OS.log_log(LOG_OS, '登陆[用户输入索引:%s]' %userinname)
        print(userinname)
        global servername


        if userinname == "['FPA']":
            LOG_OS.log_log(LOG_OS, '处理登陆事件[获取服务器地址]')
            print('获取FPA总部服务器地址...')
            # serverAddress = '127.0.0.1:6666'
            #self.serverAddress.AppendText(text='182.61.28.124:6666')
            # self.serverAddress.SetValue(text='127.0.0.1:6666')
            #self.showDialog('操作提醒','已经获取到服务器地址，请删除索引后点击登陆', size=(160, 25))
            #print('成功获取到服务器ip地址，已经复制完成，请删除你刚输入的服务器索引。')
            servername = 'FPA'
            try:
                con.open('182.61.28.124', port='6666', timeout=10)  # 正式连接服务器【这里替换为自己的IP地址或者域名】
            except:
                winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
                dlg = wx.MessageDialog(self, "连接失败\n请检查你是否输入了正确的索引（服务器名）\n或网络是否正常，如果以上情况均不存在.\n可能服务器已经不再支持当前版本，请到官网更新软件\n - www.huoyinetwork.cn", "连接失败", wx.OK)
                dlg.ShowModal()
                # self.control.SelectAll();
                dlg.Destroy()
        elif userinname == "['樱花城']":
            LOG_OS.log_log(LOG_OS, '处理登陆信息[获取服务器地址]')
            print('获取樱花城服务器地址...')
            #self.serverAddress.AppendText(text='182.61.28.124:5555')  # 独立后端
            #self.showDialog('操作提醒','已经获取到服务器地址，请删除索引后点击登陆', size=(160, 25))

            #print('成功获取到服务器ip地址，已经复制完成，请删除你刚输入的服务器索引。')
            servername = '樱花城'
            try:
                con.open('182.61.28.124', port='5555', timeout=10)  # 正式连接服务器【这里替换为自己的IP地址或者域名】
            except:
                winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
                dlg = wx.MessageDialog(self, "连接失败\n请检查你是否输入了正确的索引（服务器名）\n或网络是否正常，如果以上情况均不存在.\n可能服务器已经不再支持当前版本，请到官网更新软件\n - www.huoyinetwork.cn", "连接失败", wx.OK)
                dlg.ShowModal()
                # self.control.SelectAll();
                dlg.Destroy()
        else:
            print('连接目标服务器...')
            #LOG_OS.log_log(LOG_OS, '连接服务器[%s**%s]' %(userinname,servername))
            LOG_OS.log_log(LOG_OS, '直接连接服务器[%s]' %(userinname))
            try:
                con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)  # 正式连接服务器
            except:
                winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
                dlg = wx.MessageDialog(self, "连接失败\n请检查你是否输入了正确的索引（服务器名）\n或网络是否异常，如果以上情况均不存在.\n可能服务器已经不再支持当前版本，请到官网更新软件\n - www.huoyinetwork.cn", "连接失败", wx.OK)
                dlg.ShowModal()
                # self.control.SelectAll();
                dlg.Destroy()
            #if servername == '未识别':
            #    servername = '不明服务器'
            #    wx.StaticText(self, label="", pos=(40, 70), size=(160, 25))
            #    self.showDialog(title='连接不安全', content='即将通过不安全的方式（无索引）\n连接务器，该服务器可能处于未认证状态\n关闭窗口继续。',size=(200, 100))
            #else:
            #    pass
        #try:
        #    con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)   #正式连接服务器
        #    #PLS = str('V1.0.2')
        #    #con.write(('pls ' + PLS + '\n').encode("utf-8"))
        #except:
        #    print('出现错误，请检查网络或你的输入。')
        #    self.showDialog('错误01','连接失败\n请检查是否已删除索引或网络\n是否正常，或者服务器已经离线.' ,size=(200,100))
        #try:
        #==========写入（更新）配置
        config = configparser.ConfigParser()
        config.add_section('fpa(CN)-sr')
        # usertext = str(self.userName.GetLineText(0))
        #try:
        #ids=config.get(section='fpa(CN)-sr',option='userid')
        #ids = config.get('fpa(CN)-sr', option='userid')
        #except:
        #    print('error')
        #    ids=''
        if ids == '':
            LOG_OS.log_log(LOG_OS, '生成身份ID')
            ip2 = IP(socket.gethostbyname(socket.gethostname()))
            ip = ip2.int()
            ra = random.randint(0, 9)
            # global ID
            ID = str(ra + ip)
            print("获得身份编号:%s" % ID)
            idtime = time.strftime('%F-%H-%M-%S')
            #config = configparser.ConfigParser()
            config.set('fpa(CN)-sr', 'userid', ID)
            config.set('fpa(CN)-sr', 'idtime', idtime)
            config.set('fpa(CN)-sr', 'username', self.userName.GetLineText(0))
            config.set('fpa(CN)-sr', 'server', servername)
            NOW_path = os.getcwd()
            config.set('fpa(CN)-sr', 'path', NOW_path)
            with open('config-sr.ini', 'w') as conf:
                config.write(conf)
        else:
            ID=ids
            print('登陆身份：%s' %ID)
            idtime=time.strftime('%F-%H-%M-%S')
            config.set('fpa(CN)-sr', 'userid', ID)
            config.set('fpa(CN)-sr', 'idtime', idtime)
            config.set('fpa(CN)-sr', 'username', self.userName.GetLineText(0))
            config.set('fpa(CN)-sr', 'server', servername)
            with open('config-sr.ini', 'w') as conf:
                config.write(conf)
            #===结束====
        #except:
        #    print('诶呀，写入配置文件的时候出错啦')
        #    False_report(None,-1,title='程序出现错误了',size=(690,490),xy='Mode：LonginFrame.sz_xt',cwm='6070',fwqk=servername)
        global response
        global ponse
        response = con.read_some()  #接收服务器的第一条信息
        # ponse = response
        print('服务器支持版本：%s' % response)
        LOG_OS.log_log(LOG_OS, '版本[user:%s server:%s]' % ("V1.0.2", response))

        if response != b'V1.0.2':  # 核协议对版本==========================
            #LOG_OS.log_log(LOG_OS, '核对版本[与目标服务器版本不同]')
            print('当前版本与目标服务器版本不同，请联系管理员升级')
            self.showDialog(title='软件版本不同', content='版本信息\n本地:%s 服务器:%s\n请按情况选择升级或提醒管理员 ' %("b'V1.0.2'",response), size=(200, 100))
            num = communication_protocol
            con.write(('say ' + num + '\n').encode("utf-8"))
            return

        LOG_OS.log_log(LOG_OS, '版本[与目标服务器版本相同]')
        con.write(('login ' + str('<公测>' + self.userName.GetLineText(0)) + '\n').encode("utf-8"))
        response = con.read_some()
        if response == b'UserName Empty':
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            self.showDialog(title='Error：错误01', content='用户名不能为空！!', size=(200, 100))
        elif response == b'UserName Exist':
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            self.showDialog(title='Error：错误02', content='该用户名已存在!', size=(200, 100))
        else:
            self.Close()
            global username
            username = self.userName.GetLineText(0)
            ChatFrame(None, 2, title='FPA服务器聊天网络（%s）--%s' % (servername, username), size=(620, 420))# 加大
            #LOG_OS.log_log(LOG_OS, '加载聊天室窗口[完毕]')
        #except Exception:
        #    print('Error：连接失败01')
        #    self.showDialog('Error：连接失败01', '连接失败\n请检测网络环境或联系管理员，\n因为服务器可能已经离线.', (200, 100))  # 第一个是弹窗标题

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        LOG_OS.log_log(LOG_OS, '[错误弹出]%s' %content)
        dialog = wx.Dialog(self, title=title,size=size)
        dialog.Center()
        wx.StaticText(dialog, label='ERROR')
        wx.StaticText(dialog, label=content)
        dialog.ShowModal()
        global state
        state = '良'

    def quit(self,e):
        self.Close()
        gc.collect()
        exit()

class GengFrame(wx.Frame):
    """
    修改昵称窗口
    """

    def __init__(self, parent, id, title, size):
        LOG_OS.log_log(LOG_OS, '加载程序[初始化修改窗口，绑定按钮]')
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.icon = wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.SetSize(size)
        self.Center()
        wx.StaticText(self, label="地址: 输入服务器名称索引，软件会自动填写地址。", pos=(10, 0), size=(300, 20))
        wx.StaticText(self, label="在下方输入你的新昵称", pos=(10, 20), size=(150, 30))
        self.userNameLabel = wx.StaticText(self, label="昵称", pos=(40, 100), size=(120, 25))
        self.userName = wx.TextCtrl(self, pos=(120, 97), size=(150, 25))
        self.loginButton = wx.Button(self, label='修改', pos=(80, 145), size=(130, 30))
        # 绑定修改方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.ok)
        LOG_OS.log_log(LOG_OS, '用户执行[修改昵称]')
        self.Show()

    def ok(self,e):
        con.write(('login ' + str('<成员>' + self.userName.GetLineText(0)) + '\n').encode("utf-8"))
        response = con.read_some()
        if response == b'UserName Empty':
            self.showDialog(title='Error：错误01', content='用户名不能为空！!', size=(200, 100))
        elif response == b'UserName Exist':
            self.showDialog(title='Error：错误02', content='该用户名已被占用!', size=(200, 100))
        else:
            self.Close()
        username=self.userName.GetLineText(0)
        #ChatFrame(None, 2, title='FPA服务器聊天网络（%s）--%s' %(servername,username), size=(620, 420))
        ChatFrame(None, 2, title='FPA服务器聊天网络（%s）--%s' %(servername,username), size=(690, 440))


def helpgo(self):
    try:
        LOG_OS.log_log(LOG_OS,'用户开启帮助程序')
        #os.system('Help.exe')
        global mProcess
        mProcess = subprocess.Popen('Help.exe', stdout=subprocess.PIPE, stderr=subprocess.PIPE)#官方推荐用此模块代替os.system方法---创建一个进程运行目标程序()其中PIPE指创建一个管道
        #print(returnCode)
    except:
        print('FileError:抱歉，我们没有找到帮助程序，请确认软件包是否有丢包或被修改')

def tzzx(self):
    try:
        LOG_OS.log_log(LOG_OS, '用户开启拓展中心程序')
        #os.system('Help.exe')
        returnCode = subprocess.Popen('tzzx.exe', stdout=subprocess.PIPE, stderr=subprocess.PIPE)#官方推荐用此模块代替os.system方法---创建一个进程运行目标程序()其中PIPE指创建一个管道
        #print(returnCode)
        #以上是执行exe用的
        #os.system('python tzzx.py')
        #为了分辨
        #import tzzx.py
        #tzzx()
    except:
        os.system('kill tzzx.exe')
        #retunCode.kill()
        print('FileError:抱歉，我们没有找到帮助程序，请确认软件包是否有丢包或被修改')

'''
--按键检测(未采用)--
https://www.cnblogs.com/ajucs/p/3903690.html
https://blog.csdn.net/igolang/article/details/7870291
-----------
class KeyEvent(wx.Frame):
    def __init__(self, parent, id, title):
         wx.Frame.__init__(self, parent, id, title)
         panel = wx.Panel(self, -1)
         panel.Bind(wx.WXK_RETURN, self.OnKeyDown)
         panel.SetFocus()

         self.Centre()
         self.Show(True)

    def OnKeyDown(self, event):
         keycode = event.GetKeyCode()
         if keycode == wx.WXK_F3:
           print('66666666666666666666666')
         else:
           event.Skip()
'''


class ZanzhuFrame(wx.Frame):
    """
    赞助窗口
    """
    def __init__(self, parent, id, title, size):
        global state
        state = '优'
        # 初始化，添加控件并绑定事件
        LOG_OS.log_log(LOG_OS, ' 初始化赞助窗口')
        wx.Frame.__init__(self, parent, id, title)
        # panel = wx.Panel(window)
        # 利用wxpython的GridBagSizer()进行页面布局
        sizer = wx.GridBagSizer(0, 2)  # 列间隔为10，行间隔为20
        # 添加北京字段，并加入页面布局，为第二行，第一列
        wx.StaticText(self, label="微信                                                                                支付宝",pos=(0,15))
        wx.StaticText(self, label="请在备注注明“钱包用户赞助”以便我分辨哦~",pos=(0,0))

        #获取图片
        try:
            d = os.getcwd()  # 当前路径
            urllib.request.urlretrieve('http://www.huoyinetwork.cn/static/HO/weixin.png', "%s\\weixin.png" % d)
        except:
            print('获取最新微信二维码失败')
            dlg = wx.MessageDialog(self, '无法获取到最新的微信收款码',"获取图像失败", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        try:
            d = os.getcwd()  # 当前路径
            urllib.request.urlretrieve('http://www.huoyinetwork.cn/static/HO/zhifubao.png', "%s\\zhifubao.png" % d)
        except:
            print('获取最新支付宝二维码失败')
            dlg = wx.MessageDialog(self, '无法获取到最新的微信收款码', "获取图像失败", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

        # 获取beijing.png图片，转化为Bitmap形式，添加到第二行，第二列
        image2 = wx.Image('weixin.png', wx.BITMAP_TYPE_PNG).Rescale(320, 390).ConvertToBitmap()
        bmp2 = wx.StaticBitmap(self, -1, image2)  # 转化为wx.StaticBitmap()形式
        sizer.Add(bmp2, pos=(2, 0), flag=wx.ALL, border=5)
        # 将Panmel适应GridBagSizer()放置
        self.SetSizerAndFit(sizer)

        # 获取beijing.png图片，转化为Bitmap形式，添加到第二行，第二列
        image2 = wx.Image('zhifubao.png', wx.BITMAP_TYPE_PNG).Rescale(320, 390).ConvertToBitmap()
        bmp2 = wx.StaticBitmap(self, -1, image2)  # 转化为wx.StaticBitmap()形式
        sizer.Add(bmp2, pos=(2, 1), flag=wx.ALL, border=5)
        # 将Panmel适应GridBagSizer()放置
        self.SetSizerAndFit(sizer)

        self.Show()

class MaintFrame(wx.Frame):
    """
    主窗口
    """
    def __init__(self, parent, id, title, size):
        global state
        state = '优'
        # 初始化，添加控件并绑定事件
        LOG_OS.log_log(LOG_OS, ' 初始化主窗口，添加控件并绑定事件')
        wx.Frame.__init__(self, parent, id, title)
        self.icon = wx.Icon('%s.ico' %servername, wx.BITMAP_TYPE_ICO)  #随着服务器改变

        #载入用户设置
        LOG_OS.log_log(LOG_OS,'载入用户设置')
        config = configparser.ConfigParser()
        re = config.read('config-pyinatll.ini','utf-8')##utfutf-8便于编辑
        if os.path.isfile('config-pyinatll.ini'):
            # global background
            background = config.get('mianban', option='background')  # 背景颜色
            Typeface = config.get('mianban', option='typeface')  # 字体颜色
        else:
            background = '默认'
            Typeface = '默认'

        if background == '黑色':
            beijs = 'Black'
            self.SetBackgroundColour(beijs)
        elif background == '默认':
            t = 0
        else:
            beijs = 'White'
            self.SetBackgroundColour(beijs)

        if Typeface == '黑色':
            zhitiy = 'Black'
            self.SetForegroundColour(zhitiy)
        elif Typeface == '默认':
            t = 0
        else:
            zhitiy = 'White'
            self.SetForegroundColour(zhitiy)

        #窗口颜色
        #self.SetOwnBackgroundColour('White')
        #self.SetForegroundColour(zhitiy)
        #self.SetBackgroundColour(beijs)

        image_file = 'bj.jpg' #添加背景,由于添加背景了，所以要在下面的部分wx代码里要在self后面添加.bitmap
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))

        set_title = '%s %d x %d' % (image_file, to_bmp_image.GetWidth(), to_bmp_image.GetHeight())
        #self.button = wx.Button(self.bitmap, -1, label='Test', pos=(10,10))  加了背景后要使组建不出现意外示例
#=========菜单栏[开始]==============
        LOG_OS.log_log(LOG_OS,'创建上方菜单')
        # 创建菜单
        menuBar = wx.MenuBar()

        menu2 = wx.Menu()
        # 菜单内容&表示随后的字符为热键，参数3为在状态栏上显示的菜单项说明
        help=menu2.Append(wx.NewId(), "&发布指南", "")
        self.Bind(wx.EVT_MENU,helpgo,help)
        qiehuan=menu2.Append(wx.NewId(), "&配置码云开源", "")  #码云的授权码就是码云的私人令牌，这里我的是 928d18bdec4d3f6b2ac1f917697045e1
        self.Bind(wx.EVT_MENU, self.main_gitee,qiehuan)
        networkmenu=menu2.Append(wx.NewId(), "&配置Git开源", "")
        self.Bind(wx.EVT_MENU,self.Network_daemon,networkmenu)
        menu2.Append(wx.NewId(), "&配置PC6发布渠道", "")
        #filelook=menu2.Append(wx.NewId(), "&配置PC6发布渠道", "")
        #self.Bind(wx.EVT_MENU, self.FileLook, filelook)
        #menu2.AppendSeparator()

        news = menu2.Append(wx.NewId(), "&版本检查", "检查更新")  #升级程序后台运行，额，算了。还是在前台吧。。。
        self.Bind(wx.EVT_MENU, self.Vicx, news)
        fitem=menu2.Append(wx.NewId(), "退出", "")
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        uninst=menu2.Append(wx.NewId(), "彻底卸载程序", "")
        self.Bind(wx.EVT_MENU, self.uninstall, uninst)
        cd=menuBar.Append(menu2, "&操作菜单")
        self.SetMenuBar(menuBar)

        # 创建菜单
        #menuBar1 = wx.MenuBar()
        menu3 = wx.Menu()
        help = menu3.Append(wx.NewId(), "&帮助文档", "查看位于本地的帮助文档")
        self.Bind(wx.EVT_MENU,helpgo,help)
        menu3.Append(wx.NewId(), "&渠道提交", "向我们提交发布渠道")
        menu3.AppendSeparator()
        fankuib=menu3.Append(wx.NewId(), "&我要反馈", "向服务器发送反馈，帮助我们做得更好")
        self.Bind(wx.EVT_MENU,self.fankuiv,fankuib)
        menuBar.Append(menu3, "&获取帮助")
        self.SetMenuBar(menuBar)

        menu4 = wx.Menu()
        tuozz=menu4.Append(wx.NewId(), "&拓展中心", "管理模块")
        self.Bind(wx.EVT_MENU, tzzx, tuozz)
        menu4.AppendSeparator()
        menu4.Append(wx.NewId(), "&重新扫描", "重新扫描拓展模块")
        guiz=menu4.Append(wx.NewId(), "&开放收录功能", "相关等级规则")
        self.Bind(wx.EVT_MENU, self.Guizhe_tuoz,guiz)
        menuBar.Append(menu4, "&本地拓展功能及改进功能")   #独立出一个程序管理及运行
        self.SetMenuBar(menuBar)

        menu5 = wx.Menu()
        shezhi = menu5.Append(wx.NewId(), "&软件设置", "更改软件设置")
        self.Bind(wx.EVT_MENU,self.shezhiuiv,shezhi)
        #menu5.Append(wx.NewId(), "&网络设置", "客户端的网络调试")
        #Local_settings = menu5.Append(wx.NewId(), "&本地设置", "客户端内相关设置")
        #self.Bind(wx.EVT_MENU, self.Local_set, Local_settings)
        menu5.AppendSeparator()
        ben = menu5.Append(wx.NewId(), "&本客户端", "客户端的信息及状态")
        self.Bind(wx.EVT_MENU, self.ben_client, ben)
        menuBar.Append(menu5, "&设置")
        self.SetMenuBar(menuBar)

        #menuBar2 = wx.MenuBar()
        helpM = wx.Menu()
        # helpM.Append(wx.NewId(),"软件详情(H)", "内部详细信息")
        helpM.Append(wx.NewId(), "更新日志", "更新日志")
        fankuib = helpM.Append(wx.NewId(), "&我要反馈", "向服务器发送反馈，帮助我们做得更好")
        self.Bind(wx.EVT_MENU, self.fankuiv, fankuib)

        about = helpM.Append(wx.NewId(), "关于软件", "关于软件.")
        self.Bind(wx.EVT_MENU, self.OnAbout, about)
        helpM.AppendSeparator()
        zanzhu = helpM.Append(wx.NewId(), "赞助作者（作者块吃土了）", "作者块吃土了")
        self.Bind(wx.EVT_MENU, self.zhanzhu_s, zanzhu)
        menuBar.Append(helpM, "关于")
        # =========菜单栏[结束]==============
        #rev = str(record)

        self.SetIcon(self.icon)
        self.SetSize(size)
        self.Center()
        #wx.StaticText(self,label='当前昵称:%s' %username,pos=(10,0),size=(300,20))
        #self.chatFrame = wx.TextCtrl(self.bitmap, pos=(5, 5), size=(490, 310),value='%s\n' %rev,style=wx.TE_MULTILINE | wx.TE_READONLY)
        #self.chatFrame.SetForegroundColour('#007FFF')  #设置字体颜色
        self.chatAdmin = wx.TextCtrl(self, pos=(475, 5), size=(230, 432),value='*公测版*【打包助手】HV1.0\n____________________\n打包助手是一款帮助使用python的朋友解决项目打包不稳定、设置麻烦、进阶打包繁琐等打包问题以及项目发布渠道审核慢、不知道选哪个渠道等问题的软件，永久免费使用！\n____________________\n\n打包向导(教程)》\n【1】请完整配置好基础信息区的参数\n【2】如果您不需要进阶打包，可直接点击打包开始打包，软件将会自动完成打包（首次打包可能会比较慢，因为可能要安装打包环境），要进阶打包的请继续向下\n【3】按照实际情况填写信息（软件图标要填全名），然后点击打包\n软件执行打包的时候出现未响应仅表示窗口未响应\n____________________\n\n',style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.chatAdmin.SetForegroundColour('White')
        self.chatAdmin.SetBackgroundColour('Black')

        wx.StaticText(self, label="______________________*基础打包配置*______________________", pos=(10, 6))
        wx.StaticText(self, label="项目文件夹", pos=(10, 25))
        self.pathy = wx.TextCtrl(self, pos=(65, 25), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.fileButton = wx.Button(self, label="浏览", pos=(370, 25), size=(60, 25))
        self.fileButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.fileButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色

        wx.StaticText(self, label="文件名字", pos=(10, 55))
        self.instname = wx.TextCtrl(self, pos=(65, 55), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="清空", pos=(370, 55), size=(60, 25))
        self.closeButton.SetBackgroundColour('#EAEAAD')  # 设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  # 设置按钮字体颜色

        wx.StaticText(self, label="对外版本", pos=(10, 85))
        self.vess = wx.TextCtrl(self, pos=(65, 85), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="自动生成", pos=(370, 85), size=(60, 25))
        self.closeButton.SetBackgroundColour('#EAEAAD')  # 设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  # 设置按钮字体颜色


        self.check4 = wx.RadioButton(self, -1, "独立打包", pos=(10, 120),  style=wx.RB_GROUP)
        self.check5 = wx.RadioButton(self, -1, "关系库打包", pos=(90, 120))
        self.check6 = wx.RadioButton(self, -1, "独立去黑框打包", pos=(180, 120))

        self.fileButton.Bind(wx.EVT_BUTTON, self.OpenFile)
#        self.check1.Bind(wx.EVT_RADIOBUTTON, self.One_Play)
 #       self.check4.Bind(wx.EVT_RADIOBUTTON, self.Two_Play)

        wx.StaticText(self, label="______________________*进阶打包配置*______________________", pos=(10, 140))
        wx.StaticText(self, label="开发商", pos=(10, 160))
        self.kfs = wx.TextCtrl(self, pos=(65, 160), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="清空", pos=(370, 160), size=(60, 25))
        self.closeButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色

        wx.StaticText(self, label="描述", pos=(10, 190))
        self.mis = wx.TextCtrl(self, pos=(65, 190), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="清空", pos=(370, 190), size=(60, 25))
        self.closeButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色

        wx.StaticText(self, label="内部名称", pos=(10, 220))
        self.nnae = wx.TextCtrl(self, pos=(65, 220), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="清空", pos=(370, 220), size=(60, 25))
        self.closeButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色

        wx.StaticText(self, label="版权声明", pos=(10, 250))
        self.banquan = wx.TextCtrl(self, pos=(65, 250), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="清空", pos=(370, 250), size=(60, 25))
        self.closeButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色

        wx.StaticText(self, label="始文件名", pos=(10, 280))
        self.shifile = wx.TextCtrl(self, pos=(65, 280), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="清空", pos=(370, 280), size=(60, 25))
        self.closeButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色

        wx.StaticText(self, label="外部名称", pos=(10, 310))
        self.wname = wx.TextCtrl(self, pos=(65, 310), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="清空", pos=(370, 310), size=(60, 25))
        self.closeButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色

        wx.StaticText(self, label="软件图标", pos=(10, 340))
        self.icon = wx.TextCtrl(self, pos=(65, 340), size=(300, 25),style=wx.TE_PROCESS_ENTER)  #输入框
        self.closeButton = wx.Button(self, label="随机图标", pos=(370, 340))
        self.closeButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色

        wx.StaticText(self, label="上架版本号", pos=(5, 370))
        self.verw = wx.TextCtrl(self, pos=(65, 370), size=(300, 25), style=wx.TE_PROCESS_ENTER)  # 输入框
        self.closeButton = wx.Button(self, label="国网查询", pos=(370, 370))
        self.closeButton.SetBackgroundColour('#EAEAAD')  # 设置按钮背景颜色
        self.closeButton.SetForegroundColour('#CC7F32')  # 设置按钮字体颜色

        """
        StringStruct(u'FileDescription', u'Instant anonymous communication software'),
        StringStruct(u'FileVersion', u'V1.1.0(win10_64bit)'),
        StringStruct(u'InternalName', u'client_V1.1.0'),
        StringStruct(u'LegalCopyright', u'person. qiupeng(2018-2020).'),
        StringStruct(u'OriginalFilename', u'client.exe'),
        StringStruct(u'ProductName', u'Huoyi Internet chat room'),
        StringStruct(u'ProductVersion', u'1.1.0')])"""

        wx.StaticText(self, label="单渠道发布", pos=(96, 410))
        list1 = ['PC6资源站',  '百度','360下载','华军下载', "中关村软件"]
        dqudao = wx.ComboBox(self, -1, value='指定渠道', choices=list1, style=wx.CB_SORT,pos=(159,410))
        self.sendButton = wx.Button(self, label="发布至已配置渠道", pos=(250, 410), size=(110, 25))
        self.sendButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.sendButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色
        self.dabaoButton = wx.Button(self, label="打包", pos=(360, 410), size=(58, 25))
        self.dabaoButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.dabaoButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色
        self.dabaoButton.Bind(wx.EVT_BUTTON, self.pyinstaller_main)

        '''
        self.usersButton = wx.Button(self.bitmap, label="聊天室资讯", pos=(371, 320), size=(68, 25))
        self.usersButton.SetBackgroundColour('#EAEAAD')
        self.usersButton.SetForegroundColour('#CC7F32')

        self.closeButton.SetForegroundColour('#CC7F32')
        self.gradButton = wx.Button(self.bitmap, label="全屏截屏", pos=(490, 320), size=(100, 25))
        self.gradButton.SetBackgroundColour('#EAEAAD')
        self.gradButton.SetForegroundColour('#CC7F32')
        self.textCtrl = wx.TextCtrl(self.message, -1, value='', pos=(100, 225), size=(150, 25))
        '''

        self.closeButton = wx.Button(self, label="退出", pos=(426, 410), size=(48, 25))
        self.closeButton.Bind(wx.EVT_BUTTON, self.Quite)
        self.sendButton.SetBackgroundColour('#EAEAAD')  #设置按钮背景颜色
        self.sendButton.SetForegroundColour('#CC7F32')  #设置按钮字体颜色
        '''
        #按键检测（回车发送）
        self.Bind(wx.EVT_TEXT_ENTER, self.send, self.message)

        # 发送按钮绑定发送消息方法
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)
        # Users按钮绑定获取在线用户数量方法
        self.usersButton.Bind(wx.EVT_BUTTON, self.lookUsers)
        #截屏
        self.gradButton.Bind(wx.EVT_BUTTON,self.grad)
        # 关闭按钮绑定关闭方法
        self.closeButton.Bind(wx.EVT_BUTTON, self.Quite)

        thread.start_new_thread(self.receive, ())
        '''
        LOG_OS.log_log(LOG_OS,'初始化完成')
        self.chatAdmin.AppendText('程序初始化完成！\n')
        self.Show()

        self.chatAdmin.AppendText('正在检查软件版本..\n')
        try:
            global ver_nei
            ver_news, ver_log, ver_ei = self.Version_checking()
            ver_nei = (ver_ei[:-1])  # 去除最后面的英文逗号'得到正确的后缀名
            if ver_news == "b'%s" % ver:
                self.chatAdmin.AppendText('\n[*恭喜*]您当前使用的是最新版本，无需更新！\n如果您的软件不能正常使用，可以继续下载最新版程序，我们将覆盖现有程序以尝试修复错误。\n')
            else:
                self.chatAdmin.AppendText('[*注意*]有可用更新！！\n最新版本：%s\n新版本简介：%s\n' % (ver_news, ver_log))
                dlg = wx.MessageDialog(self, '[*注意*]有可用更新！！\n最新版本：%s\n新版本简介：%s\n' % (ver_news, ver_log),"有新版本，建议更新哦~" , wx.OK)
                #dlg.ShowModal()
                if dlg.ShowModal() == wx.ID_OK:
                    self.Vicx(self)
                dlg.Destroy()
        except:
            self.chatAdmin.AppendText('[*异常*]检查版本失败！！\n我们不能获取到服务器的帮助和支持，如有需要请检查网络情况并重启软件。\n')
            dlg = wx.MessageDialog(self, '检查版本失败！！\n我们不能获取到服务器的帮助和支持，如有需要请检查网络情况并重启软件。\n', "网络异常",wx.OK)
            dlg.ShowModal()
            #dlg.Destroy()
        #print(ver_news)
        #print(ver_log)

    def Version_checking(self):
        LOG_OS.log_log(LOG_OS,"运行版本检查")
        try:
            client = socket.socket()  # 生成socket连接对象
            ip_port = ("106.12.103.112", 6979)  # 地址和端口号 填localhost可以进行本地测试【这里替换为自己的IP地址或者域名】
            client.connect(ip_port)  # 连接
        except:
            LOG_OS.log_log(LOG_OS,"[%s]状态：连接服务器失败！3秒后退出..." %(time.strftime("%F %H:%M:%S")))

        else:
            LOG_OS.log_log(LOG_OS,"[%s]状态：服务器连接成功!" %(time.strftime("%F %H:%M:%S")))
        bit = struct.calcsize("P") * 8
        content = ("Verg 1215")
        client.send(content.encode("utf-8"))  # 传送和接收都是bytes类型
        time.sleep(1)
        # 1.先接收长度，建议8192
        server_response = client.recv(1024)
        new_ver,gx_log,gx_nei = str(server_response).split('@')
        #new_ver = str(server_response.decode("utf-8"))
        client.close()
        return new_ver,gx_log,gx_nei

    def OpenFile(self, event):
        '''
        打开开文件对话框（浏览文件）
        '''
        file_wildcard = ""
        dlg = wx.FileDialog(self, "选择项目文件夹",
                            os.getcwd(),
                            style=wx.OS_UNIX_OPENBSD,
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()  # 获取文件路径
            print('path:', self.filename)  # 打印路径
            self.pathy.write(self.filename)  # 将路径发送到输入框
            # self.ReadFile()
            self.SetTitle(self.title + '--' + self.filename)

        dlg.Destroy()

    def zhanzhu_s(self,e):
        ZanzhuFrame(None, -1, title='赞助作者', size=(690, 490))

    def Local_set(self,event):
        try:
            root = tkinter.Tk()  # 创建一个Tkinter.Tk()实例
            root.withdraw()  # 将Tkinter.Tk()实例隐藏 否则会留下一个小框

            path = os.getcwd()
            filename = filedialog.askopenfilename(initialdir=path)
            print(filename)
        except:
            dlg = wx.MessageDialog(self, '抱歉，加载本地设置控制面板的时候出现了一些错误，导致我们无法启动该面板，十分抱歉', "加载失败", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

    def ben_client(self,event):
        LOG_OS.log_log(LOG_OS, '用户查看客户端信息及状态')
        me = sys.argv[0]
        print(me)
        hou = str(os.path.splitext(me)[1])
        print(hou)
        global init
        init = '检查失败'
        if hou == '.py':
            init = '源码调试'
        else:
            init = '成品运行'
        for proc in psutil.process_iter():
            pidn,pida = proc.pid, proc.name()
        dlg = wx.MessageDialog(self, '''软件版本：V1.1.0（公测版）
        软件被安装在：%s
        运行状态：%s
        主程序PID：%s
        进程名：%s
        ''' % (os.getcwd(),init,pidn,pida), "运行数据", wx.OK)
        dlg.ShowModal()
        # self.control.SelectAll();
        dlg.Destroy()

    def OnAbout(self, event):
        LOG_OS.log_log(LOG_OS,'用户查看软件信息')
        dlg = wx.MessageDialog(self, '''软件版本：%s
---打包助手是一个中文语境下的轻型项目发布和开源软件
是作者利用闲余时间，在宿舍完善的。软件轻便，目前内测仅支持在windows设备运行，同时支持部分的开源渠道和发布渠道上传。
开放收录功能函数，具体详情请点击“本地拓展”-》“开放收录功能”
核心版本: FPN.pyinstall.0.1
软件作者: 无别（QQ：2048408982）
软件被安装在：%s        ''' %(ver,os.getcwd()), "关于软件", wx.OK)
        dlg.ShowModal()
        #self.control.SelectAll();
        dlg.Destroy()

    def fankuiv(self,e):
        False_fankui(None,-1,title='用户反馈')

    def shezhiuiv(self,e):
        shezhi(None,-1,title='软件设置')

    def pyinstaller_main(self,e):
        fgh = 0
        try:
            global path
            path = self.pathy.GetLineText(0)
            instname = self.instname.GetLineText(0)
            print(path)
            pd = ('%s\打包日志' % path)
            print(os.path.exists(pd))
            if os.path.exists(pd):
                print('环境基本符合要求')
                self.chatAdmin.AppendText('(^u^)打包环境检查通过！\n')
            else:
                os.makedirs('%s\打包日志' % path)
                file = open('%s\instlog.txt' % pd, 'a')
                file.write('[打包助手%s]/打包日志\n[项目：%s]新建打包日志\n' %(veri,instname))
                file.close()
        except:
            print('环境不符合要求，正在尝试修复..')
            self.chatAdmin.AppendText('Σ(ﾟдﾟ)打包环境检查失败！\n原因：\n1.您的文件路径不完整或者填写错误。')
            fgh = 103
        try:#打包前环境检查
            import PyInstaller
            file = open('%s\instlog.txt' %pd, 'a')
            file.write('[INFO]PyInstaller是否安装\n' )
            file.close()
        except:
            print('环境不符合要求，正在尝试修复..')
            self.chatAdmin.AppendText( 'Σ(ﾟдﾟ)打包环境检查失败！\n可能原因：\n1.您的电脑中没有安装pyinstaller模块，软件会尝试安装该模块，请保持网络通畅。\n2.您的电脑未正确配置环境变量和pip。')
            file = open('%s\instlog.txt' %pd, 'a')
            file.write('[ERROR]PyInstaller未安装\n')
            file.close()
            xiufu = str(os.system('python -m pip install PyInstaller'))
            file = open('%s\instlog.txt' %pd, 'a')
            file.write('[INFO]安装PyInstaller模块完成【返回%s】\n' %xiufu)
            file.close()
            if xiufu == '0':
                print('命令执行成功，请再次尝试打包\n')
                self.chatAdmin.AppendText('(^u^)命令执行成功，请再次尝试打包\n')

            else:
                print('Σ(ﾟдﾟ)命令执行失败，请检查您的python是否存在于系统的PATH变量中，或pip是否安装\n')
                self.chatAdmin.AppendText('Σ(ﾟдﾟ)命令执行失败，请检查您的python是否存在于系统的PATH变量中，或pip是否安装\n')
                fgh = 101

        if instname == '':
            print('项目名不能为空！')
            self.chatAdmin.AppendText('(*’ｰ’*)项目名不能为空！\n')
            return
        if fgh != 0:
            print('【中断】环境错误！')
            self.chatAdmin.AppendText('【中断】环境错误！\n')
            file = open('%s\instlog.txt' %pd, 'a')
            file.write('[ERROR]环境错误，中断操作\n')
            file.close()
            return
        LOG_OS.pyinstalllog(LOG_OS, pd, '[INFO]开始打包')
        self.chatAdmin.AppendText('生成预处理文件...\n')
        cmd1 =( '''@echo off
cd %s
python -m PyInstaller -F %s\%s.py
        ''' %(path,path,instname))
        jiaoben = open('inst.bat','w')
        jiaoben.write(cmd1)
        jiaoben.close()
        self.chatAdmin.AppendText('开始打包,请耐心等待...\n')
        #cmdjg = str(os.system('python -m PyInstaller -F %s\main.py' %path))
        cmdjg = str(os.system('%s\inst.bat' %(os.getcwd())))
        print(cmdjg)
        LOG_OS.pyinstalllog(LOG_OS, pd, '[WEIZ]打包结束【结果%s】\n' %cmdjg)
        os.remove('%s\inst.bat' %(os.getcwd()))
        if cmdjg != '0':
            print('基础打包失败！')
            self.chatAdmin.AppendText('Σ(ﾟдﾟ)啊！十分抱歉，打包失败了，请再次检查您的配置和环境。\n')
        else:
            print('基础打包成功！')
            self.chatAdmin.AppendText('(ﾉ>ω<)ﾉ恭喜，您的项目已经完成打包！主程序位置:%s\dist\%s.exe\n_____________________\n' %(path,instname))
            file = open('%s\instlog.txt' % pd, 'a')
            file.write('[INFO]打包成功，主程序位置:%s\dist\%s.exe\n' %(path,instname))
            file.close()

        kaifashang = self.kfs.GetLineText(0)
        if kaifashang != '' or kaifashang != ' ':
            self.chatAdmin.AppendText("您似乎配置了进阶打包，准备填写信息并开始进阶打包\n")
            LOG_OS.pyinstalllog(LOG_OS,pd,'[INFO]用户可能配置了进阶打包，开始填写信息')
            maioshu = self.mis.GetLineText(0)
            nname = self.nnae.GetLineText(0)
            banquna = self.banquan.GetLineText(0)
            sname = self.shifile.GetLineText(0)
            wname = self.wname.GetLineText(0)
            icon = self.icon.GetLineText(0)#唯一上架版本号

            self.chatAdmin.AppendText("修改SPEC\n")
            LOG_OS.pyinstalllog(LOG_OS, pd, '[INFO]修改SPEC\n')
            specfile = open("%s/%s.spec" %(path,instname)) #完成spec文件的修改
            yuan = specfile.read().split('          [],')
            specfile.close()
            now = ("""%s          version='version.txt',
          icon='%s',
          %s""" %(yuan[0],icon,yuan[1]))
            spesfilet = open("%s/%s.spec" %(path,instname),'w')
            spesfilet.write(now)
            spesfilet.close()

            self.chatAdmin.AppendText("创建version.txt\n")
            LOG_OS.pyinstalllog(LOG_OS, pd, '[INFO]创建version.txt')
            #完version.txt的创建
            verss = self.vess.GetLineText(0)
            verws = self.verw.GetLineText(0)
            versiontext = ("""# UTF-8
#
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=(1, 1, 0, 101),
    prodvers=(1, 1, 0, 101),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x40004,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'%s'),
        StringStruct(u'FileDescription', u'%s'),
        StringStruct(u'FileVersion', u'%s'),
        StringStruct(u'InternalName', u'%s'),
        StringStruct(u'LegalCopyright', u'%s'),
        StringStruct(u'OriginalFilename', u'%s'),
        StringStruct(u'ProductName', u'%s'),
        StringStruct(u'ProductVersion', u'%s')])
      ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)""" %(kaifashang,maioshu,verss,nname,banquna,sname,wname,verws))# maioshu   nname   banquna   sname  wname
            self.chatAdmin.AppendText("写入version.txt\n")
            LOG_OS.pyinstalllog(LOG_OS, pd, '[INFO]写入version.txt')
            verssfile = open("%s/version.txt" %path,'a')
            verssfile.write(versiontext)
            verssfile.close()
            self.chatAdmin.AppendText("当前模式下，我们认为您的项目将发布出去，所以默认独立打包，去除边框\n")
            self.chatAdmin.AppendText('生成预处理文件...\n')
            cmd1 = ('''@echo off
cd %s
python -m PyInstaller  -F -w %s.py
python -m PyInstaller  %s.spec --noconsole
                ''' % (path,instname, instname))
            jiaoben = open('inst.bat', 'w')
            jiaoben.write(cmd1)
            jiaoben.close()
            self.chatAdmin.AppendText('开始打包,请耐心等待...\n')
            # cmdjg = str(os.system('python -m PyInstaller -F %s\main.py' %path))
            cmdjg = str(os.system('%s\inst.bat' % (os.getcwd())))
            print(cmdjg)
            LOG_OS.pyinstalllog(LOG_OS, pd, '[WEIZ]打包结束【结果%s】' % cmdjg)
            os.remove('%s\inst.bat' % (os.getcwd()))
            if cmdjg != '0':
                print('进阶打包失败！')
                self.chatAdmin.AppendText('Σ(ﾟдﾟ)啊！十分抱歉，打包失败了，请再次检查您的配置和环境。\n')
            else:
                print('进阶打包成功！')
                self.chatAdmin.AppendText('(ﾉ>ω<)ﾉ恭喜，您的项目已经完成打包！主程序位置:%s\dist\%s.exe\n_____________________\n' %(path,instname))
                file = open('%s\instlog.txt' % pd, 'a')
                file.write('[INFO]打包成功，主程序位置:%s\dist\%s.exe\n' %(path,instname))
                file.close()

    def main_gitee(self,e):#gitee发布配置模块（码云）配置参数
        giteeapishezhi(None, -1, title='配置您的码云接口')

    def uninstall(self,e):  #彻底卸载程序
        LOG_OS.log_log(LOG_OS,'[彻底卸载程序]用户点击彻底卸载')
        r = wx.MessageBox("嘤嘤嘤~你真的要卸载我吗？此操作会彻底删除本地有关文件。", "操作不可逆转", wx.CANCEL | wx.OK | wx.ICON_QUESTION)
        if r == wx.ID_OK:
            self.Destroy()
        if r == wx.OK:
            print('卸载中...')
            dlg=wx.MessageDialog(self, '我们有缘再见，希望下次再见可以让你满意', "再见~", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            #
            #
            os.removedirs('E:\FPA_OS')
            #
            #生成bat脚本，脚本终止程序，然后再删除当前工作文件夹，避免文件占用
            bat_s='''
            cd /d %~dp0
            kill /f /im client(V1.1.0).exe
            rd
            for /f "delims=" %%i in ('dir /s/b/a-d *?????*') do (
                set f=%%~nxi
                echo.%%i
                set f=!f:?????= !
                ren "%%i" "!f!"
            )
             '''
            f = open('C:\\bat_un.bat','w')
            f.write(bat_s)
            f.close()
            os.system('C:\\bat_un.bat')
            path_not= os.getcwd()
            os.removedirs('%s' %path_not)#删除
            exit()

        else:
            print('谢谢~你真好')
            dlg=wx.MessageDialog(self, '谢谢你留下我~~', "谢谢你~", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

    def Network_daemon(self,event):  #网络守护（软件作者：防掉线功能可自由开发然后命名为Networkdaemon.py）
        print('网络守护进程开启中...')
        try:
            #import Networkdaemon
            #Networkdaemon.daemon_main() #启动库里面的守护主程序
            global netde
            netde=subprocess.Popen('python Networkdaemon.py', shell = True)
        except:
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            netde.kill()
            print('本地无网络守护插件，启动基础版守护程序...')
            time.sleep(1)

    def Guizhe_tuoz(self, event):
        LOG_OS.log_log(LOG_OS,'用户查看收录规则信息')
        dlg = wx.MessageDialog(self,'''软件初期并没有太多的功能，
但是！众人拾柴火焰高，我们公开收录功能代码：
具体收录要求如下：
1.实现的功能，除了不能违法外，暂时没有限制
2.代码可以在pythob3版本运行或bat文件
3.代码包含合理注释
4.允许代码中提交您的开发者信息，我们会展示它们
5.不得包含违法功能
（看到软件菜单栏上方的哪些没有实现的功能了吗，
团队最近忙于其他项目，该项目没有花太多时间，有
兴趣了可以尝试实现一下）

如何提交？
将代码编写完成并本地测试后，作为附件，通过邮箱发
送到 huoyiyun@qq.com 邮箱（这里也接收各种建议），
邮件内容备注以下
开发者（作者或团队，如：小天）
代码功能（如：提交项目到PC6发布）
代码测试环境和库（如：在py3+requests 2.5.6环境下运行正常）

PS：您随时可以要求我们下架您提交的功能
     打包助手开发团队（火毅网络[www.huoyinetwork.cn]） 宣''', "开放收录规则", wx.OK)
        dlg.ShowModal()
        #self.control.SelectAll();
        dlg.Destroy()

    def Vicx(self,e):
        print('启动更新模块...') #更新程序将下载对应操作系统的软件压缩包（64/32）并以覆盖的方式解压到当前文件夹
        LOG_OS.log_log(LOG_OS,'[用户执行]更新客户端')
        time.sleep(1)
        dlg = wx.MessageDialog(self, "本客户端版本：V1.1.0\n通讯协议: FPA1.0.2-\n程序将会连接版本服务器获取最新版本程序压缩包\n并自动覆盖当前软件（如果是最新版则修复客户端）\n点击ok开始更新","软件更新检查程序", wx.OK)
        dlg.ShowModal()
        # self.control.SelectAll();
        dlg.Destroy()

        try:
            LOG_OS.log_log(LOG_OS, '用户开启更新程序')
            # os.system('Help.exe')
            LOG_OS.log_log(LOG_OS, '[更新模块]启动新进程进行更新')
            os.system('UpMode.exe')
            #os.system('python -m UpMode.py')
            #mProcess = subprocess.Popen('UpMode.py', stdout=subprocess.PIPE,stderr=subprocess.PIPE)  # 官方推荐用此模块代替os.system方法---创建一个进程运行目标程序()其中PIPE指创建一个管道
            # print(returnCode)
        except:
            winsound.PlaySound("s01.wav", winsound.SND_ASYNC)
            print('FileError:抱歉，我们没有找到升级程序，请确认软件包是否有丢包或被修改')
            LOG_OS.log_log(LOG_OS,'[FileError]抱歉，没有找到帮助程序，请确认软件包是否有丢包或被修改')
            dlg = wx.MessageDialog(self, "FileError:抱歉，我们没有找到帮助程序，请确认软件包是否有丢包或被修改", "[更新模块不存在]", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()



    def Dialog(self, title, content, size):
        # 显示提示信息对话框
        LOG_OS.log_log(LOG_OS, '[操作提示或帮助]%s' % content)
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label='操作提示或帮助')
        wx.StaticText(dialog, label=content)
        dialog.ShowModal()

    def onClick(self, evt):
        dialog = wx.Dialog(self.panel)
        rec = dialog.ShowModal()

    def OnQuit(self, e):
        print('Exit。。。。。')
        # 关闭窗口并退出===菜单栏调用部分
        LOG_OS.log_log(LOG_OS, '用户执行[关闭窗口并退出-菜单栏]')
        gc.collect()
        self.Close()
        try:
            LOG_OS.log_log(LOG_OS, '退出程序[关闭帮助程序进程]')
            #os.system('kill tzzx.py')
            #subprocess.Popen.kill(self)
            #mProcess.terminate()  #关闭帮助程序产生的进程
        except:
            LOG_OS.log_log(LOG_OS, '退出程序[用户未启动帮助程序或关闭失败]')
            pass
        #try:
        #    LOG_OS.log_log(LOG_OS, '退出程序[关闭拓展中心进程]')
        #    os.system('kill tzzx.exe') #关闭拓展中心的进程
        #    #subprocess.Popen.kill(self)
        #except:
        #    LOG_OS.log_log(LOG_OS, '退出程序[用户未启动拓展中心或关闭失败]')
        #    pass
        LOG_OS.log_log(LOG_OS, '退出程序[终止程序]')
        exit()

    def FileLook(self,e):
        path = r'C:/FPA_OS/log/'
        os.startfile(path)
        LOG_OS.log_log(LOG_OS, '[用户执行]查看日志缓存')
        #os.system("explorer C:/FPA_OS")

    def qiehuan(self,e):
        LOG_OS.log_log(LOG_OS, '[用户执行]修改在线昵称')
        self.Dialog(title='修改昵称', content='正在重新连接中，成功登陆\n服务器后请保留原服务器界面。\n该功能非正常运行如果给您带来不便，\n望谅解。', size=(260, 100))
        LOG_OS.log_log(LOG_OS, '[用户确认]修改在线昵称')
        GengFrame(None, -1, title=Program_version, size=(320, 250))
        LOG_OS.log_log(LOG_OS, '[系统执行]在线昵称更换')
        #time.sleep(4)
        #ex=self.close
        #LoginFrame(None, -1, title=Program_version, size=(320, 250))

    def ztcs(self, sta):
        # 修改状态
        LOG_OS.log_log(LOG_OS, '用户端执行[修改状态]')
        state = ('连接状态：%s' % sta)
        self.chatAdmin.AppendText(state)
        # print('ok')

    def grad(self,event):    #实现全屏截屏
        print('截屏...')
        LOG_OS.log_log(LOG_OS, '用户执行[截屏]')
        try:
            im = ImageGrab.grab()
            nowtime  = time.strftime('%M%S')
            im.save('C:/FPA_OS/截屏目录/截屏%s.jpeg' %nowtime)  #保存
            LOG_OS.log_log(LOG_OS, '截屏完成[保存成功]')
        except:
            print('错误04：无法完成截屏！')
            LOG_OS.log_log(LOG_OS, '截屏失败[保存失败]')
            #self.showTips('截屏错误04','无法完成截屏\n可能是路径错误，关闭窗口开始修复。')
            print('无法完成截屏\n可能是路径错误，开始修复.....')
            LOG_OS.log_log(LOG_OS, '截屏失败[尝试修复]')
            time.sleep(1)
            os.makedirs('C:/FPA_OS/截屏目录')
            time.sleep(1)
            print('提示！路径错误已修复完成！')
            LOG_OS.log_log(LOG_OS, '截屏失败[修复完成]')
            #self.showTips('提示','路径错误已修复完成')
        else:
            print('截屏已完成，保存于‘C:/FPA_OS/截屏目录’下')
            #self.showTips('提示','截屏已完成，保存于截屏目录下。')





    def lookUsers(self, event):
        # 查看当前在线用户
        LOG_OS.log_log(LOG_OS, '用户执行[查看在线用户]')
        con.write(b'look\n')
        self.ztcs(sta='优')

    def Quite(self, event):
        # 关闭窗口并退出
        print('Exit1。。。。')
        LOG_OS.log_log(LOG_OS, '用户执行[关闭窗口并退出-按钮]')
        #con.write(b'logout\n')
        #con.close()
        gc.collect()
        self.Close()
        try:
            LOG_OS.log_log(LOG_OS, '退出程序[关闭帮助程序进程]')
            # os.system('kill tzzx.py')
            # subprocess.Popen.kill(self)
            #mProcess.terminate()  # 关闭帮助程序产生的进程
        except:
            LOG_OS.log_log(LOG_OS, '退出程序[用户未启动帮助程序或关闭失败]')
            pass
        #try:
        #    LOG_OS.log_log(LOG_OS, '退出程序[关闭拓展中心进程]')
        #    os.system('kill tzzx.py')  # 关闭拓展中心的进程
        #    # subprocess.Popen.kill(self)
        #except:
        #    LOG_OS.log_log(LOG_OS, '退出程序[用户未启动拓展中心或关闭失败]')
        #    pass
        LOG_OS.log_log(LOG_OS, '退出程序[终止程序]')
        exit()


    def showTips(title, content, size):
        # 显示错误信息对话框
        LOG_OS.log_log(LOG_OS, '提示[%s]' %content)
        dialog = wx.Dialog(title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label='提示')
        wx.StaticText(dialog, label=content)
        dialog.ShowModal()
        global state
        state = '良'

    def receive(self):
        # 接受服务器的消息
        LOG_OS.log_log(LOG_OS, '服务器[发送了一条指令]')
        while True:
            #sleep(0.4)  #刷新频率
            try:
                s=float(times)  #可设置的频率
            except:
                s = 0.3  # 默认频率（由于判断错误会消耗时间，所以缩短了默认延迟）
                LOG_OS.log_log(LOG_OS,'[接受消息]设置的刷新频率错误(%s)，使用默认频率。' %s)
            #s=int(times)
            sleep(s)  #刷新频率
            result = con.read_very_eager()
            if result != '':
                self.chatFrame.AppendText(result)
                ne = str(result)
                if ne == b'exits':
                    LOG_OS.log_log(LOG_OS, '[系统消息]全体退出')
                    print('[系统消息]全体退出')
                    self.chatFrame.AppendText('[系统消息]管理员发出全体退出指令\n[本地中控]小羽：由于你是管理员，所以不会退出。')
                    time.sleep(3)
                    self.Close()
                    LOG_OS.log_log(LOG_OS,'关闭窗口完成')
                    exit()
                elif ne == "b'EXITS'":
                    LOG_OS.log_log(LOG_OS, '[系统消息]全体退出')
                    print('[系统消息]全体退出')
                    self.chatFrame.AppendText('[系统消息]管理员发出全体退出指令\n[本地中控]小羽：由于你是管理员，所以不会退出。')
                    time.sleep(3)
                    self.Close()
                    LOG_OS.log_log(LOG_OS,'关闭窗口完成')
                    exit()
                elif ne == "exits":
                    LOG_OS.log_log(LOG_OS, '[系统消息]全体退出')
                    print('[系统消息]全体退出')
                    self.chatFrame.AppendText('[系统消息]管理员发出全体退出指令\n[本地中控]小羽：由于你是管理员，所以不会退出。')
                    time.sleep(3)
                    self.Close()
                    LOG_OS.log_log(LOG_OS,'关闭窗口完成')
                    exit()
                elif ne != "b''":
                    winsound.PlaySound("s02.wav", winsound.SND_ASYNC)
                    LOG_OS.log_log(LOG_OS, '服务器[发送了一条新消息]')
                    #speaker.Speak('新消息')
                    self.ztcs(sta='优')

                    neStr = result.decode('utf-8')  # 用什么格式编码就需要用同样格式去解码，否则出错

                    #Chat_OS.Chat_wr(Chat_OS,'%s' %neStr)
                    # print(ne)   #打印消息
                else:
                    pass




if __name__ == '__main__':
    app = wx.App()
    con = telnetlib.Telnet()
    LOG_OS.log_log(LOG_OS, '加载程序[主程序]')
    MaintFrame(None, 2, title='打包助手', size=(720, 520))
    #LoginFrame(None, -1, title=Program_version, size=(340, 320))

    app.MainLoop()
