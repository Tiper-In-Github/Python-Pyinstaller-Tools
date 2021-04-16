#更新模块
#coding=utf-8
#内测版
#非独立运行

import wx
import zipfile
import socket
import os
import hashlib
import time
import struct #用于返回操作系统的位数，其余信息可通过os返回，这里该程序是为了升级，可以用这个
import winsound
import subprocess
import sys

ver = 'V1.0.2'
#ver = 'V1.0.2'

class LOG_OS():  #文件系统

    def log_log(self,event):  #运行日志
        try:
            LOG_FILE = open('C:/FPA_OS/log/log_file_user.txt', 'a+')
        except:
            print('文件夹缺失，正在修复...')
            print('[首次运行]创建环境')
            os.makedirs('C:/FPA_OS/log')
            os.makedirs('C:/FPA_OS/Chat/')
            os.makedirs('C:/FPA_OS/folder/')
            print('修复完成')
            LOG_FILE = open('C:/FPA_OS/log/log_file_user.txt', 'a+')
            t = time.strftime('%F %H:%M:%S')
            LOG_FILE.write('[%s][文件系统][首次运行]新建程序专用文件夹（<C:/FPA_OS><C:/FPA_OS/log><C:/FPA_OS/Chat><C:/FPA_OS/folder>）\n' %t)
            LOG_FILE.write('[首次运行]程序路径：%s\n' %os.getcwd())
            LOG_FILE.close()
        f = str(event)
        t = time.strftime('%F %H:%M:%S')
        text = ('[:%s]Event:%s \n' % (t, f))
        LOG_FILE.write(text)
        LOG_FILE.close()
        pass

class customStatusBar(wx.StatusBar):
    def __init__(self, parent,num):
        wx.StatusBar.__init__(self,parent,-1)
        self.SetFieldsCount(2)
        self.SetStatusWidths([-2,-1])
        self.count=0
        #print(parent.GetSize())
        self.gauge=wx.Gauge(self,1001,100,pos=(2,2),size=(parent.GetSize()[0],20),style = wx.GA_HORIZONTAL)
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.gauge.SetValue(num)

def updateProgress(self):
    self.count += 1
    if self.count >= 20:
        self.Destroy()
    self.progress.SetValue(self.count)
class MainFrame(wx.Frame):
    """
    窗口
    """

    def __init__(self, parent, id, title, size):
        LOG_OS.log_log(LOG_OS, '更新模块[初始化操作窗口，绑定按钮]')
        # 初始化，添加控件并绑定事件

        wx.Frame.__init__(self, parent, id, title)
        self.icon = wx.Icon('up.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.SetSize(size)
        self.Center()

        #添加背景 #添加背景,由于添加背景了，所以要在下面的部分wx代码里要在self后面添加.bitm
        #image_file = 'bj.jpg' #添加背景 #添加背景,由于添加背景了，所以要在下面的部分wx代码里要在self后面添加.bitm
        #to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
        #image_width = to_bmp_image.GetWidth()
        #image_height = to_bmp_image.GetHeight()
        #set_title = '%s %d x %d' % (image_file, to_bmp_image.GetWidth(), to_bmp_image.GetHeight())


        #self.button = wx.Button(self.bitmap, -1, label='Exit', pos=(10,10))

        #bmp = wx.Image("send.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        #self.button = wx.BitmapButton(None, -1, bmp, pos=(10, 20))
        #self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        #self.button.SetDefault()
        #self.button2 = wx.BitmapButton(None, -1, bmp, pos=(100, 20),style=0)
        #self.Bind(wx.EVT_BUTTON, self.OnClick, self.button2)

        #ti = time.strftime('%F %H:%M:%S')
        #wx.StaticText(self,label="报告文档将不会包含除时间及你稍后填写的内容外的其他任何信息\n如果可以，请在描述完后留下联系方式（微信、QQ、电话、邮箱），作者会在48小时（一般12小时）内回复你。\nTime:%s" % ti,pos=(400, 30), size=(220, 330))
        self.yhmsLabel = wx.StaticText(self, label="你的遇到了什么问题或不方便？又或者希望软件在哪方面进行改进？", pos=(40, 100), size=(120, 25))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY, pos=(6,5), size=(620, 320), value='''
◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
( *・ω・)✄╰ひ╯
升级模块：该模块将帮助你完成软件的更新、升级或修复。
版本状态：
    当前版本：b''%s'
抱歉：我们没能使新版本的中文解释信息直接在服务器与客户端之间传递，因此以下在线内容均为英文，带来不便
(。﹏。*)′-一┳═┻︻▄敬请谅解！！！


        ''' %ver)

        #self.portButton = wx.Button(self, label='反   馈', pos=(20, 345), size=(379, 30))
        self.check1 = wx.RadioButton(self,-1,"更新后自动重启",pos = (5,340),size = (99,20))
        self.verjcButton = wx.Button(self, label='检查更新', pos=(110, 340), size=(160, 30))
        self.xiazaiButton = wx.Button(self, label='下载最新版', pos=(290, 340), size=(160, 30))
        self.quitssButton = wx.Button(self, label='退 出 模 块', pos=(460, 340), size=(160, 30))
        self.verjcButton.Bind(wx.EVT_BUTTON,self.ver_sss)
        self.xiazaiButton.Bind(wx.EVT_BUTTON,self.Up_qd)
        self.quitssButton.Bind(wx.EVT_BUTTON,self.quit)
        LOG_OS.log_log(LOG_OS, '更新模块[初始化完成]')
        self.Show()

    # 编写bat脚本，删除旧程序，运行新程序
    def WriteRestartCmd(self,exe_name):
        b = open("upgrade.bat", 'w')
        TempList = "@echo off\n"  # 关闭bat脚本的输出
        TempList += "if not exist " + exe_name + " exit \n"  # 新文件不存在,退出脚本执行
        TempList += "sleep 3\n"  # 3秒后删除旧程序（3秒后程序已运行结束，不延时的话，会提示被占用，无法删除）
        TempList += "del " + os.path.realpath(sys.argv[0]) + "\n"  # 删除自己
        TempList += "del " + os.getcwd()+ '\火毅匿名聊天室.exe' + "\n"  # 删除主程序
        TempList += "del " + os.getcwd()+ '\Help.exe' + "\n"  # 删除帮助程序
        TempList += "start " + exe_name  # 启动新程序
        b.write(TempList)
        b.close()
        subprocess.Popen("upgrade.bat")
        sys.exit()  # 进行升级，退出此程序

    def zdgx_main(self):
        # 新程序启动时，删除旧程序制造的脚本
        if os.path.isfile("upgrade.bat"):
            os.remove("upgrade.bat")
        self.WriteRestartCmd("火毅匿名聊天室.exe")

    def ver_sss(self,e):
        self.control.AppendText('正在检查软件版本..\n')
        global ver_nei
        ver_news,ver_log,ver_ei = self.Version_checking()
        ver_nei = (ver_ei[:-1]) #去除最后面的英文逗号'得到正确的后缀名
        if ver_news == "b'%s" %ver:
            self.control.AppendText('\n[*恭喜*]您当前使用的是最新版本，无需更新！\n如果您的软件不能正常使用，可以继续下载最新版程序，我们将覆盖现有程序以尝试修复错误。\n')
        else:
            self.control.AppendText('[*注意*]有可用更新！！\n最新版本：%s\n新版本简介：%s\n' %(ver_news,ver_log))
        print(ver_news)
        print(ver_log)

    def showDialog(self, title, content, size):
        # 显示对话框
        LOG_OS.log_log(LOG_OS, '[错误弹出]%s' % content)
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label='ERROR')
        wx.StaticText(dialog, label=content)
        dialog.ShowModal()

    def customStatusBar(self,parent,num):
        wx.StatusBar.__init__(self, parent, -1)
        self.SetFieldsCount(2)
        self.SetStatusWidths([-2, -1])
        self.count = 0
        print(parent.GetSize())
        self.gauge = wx.Gauge(self, 1001, 100, pos=(2, 2), size=(parent.GetSize()[0], 20), style=wx.GA_HORIZONTAL)
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.gauge.SetValue(num)

    def quit(self,e):
        LOG_OS.log_log(LOG_OS, '更新模块[用户退出模块]')
        time.sleep(1)
        self.Close()
        exit()

    def Up_qd(self,e):
        r = wx.MessageBox("软件开始下载最新版客户端//修复客户端，是否继续？。", "软件更新//修复错误", wx.CANCEL | wx.OK | wx.ICON_QUESTION)
        LOG_OS.log_log(LOG_OS, '更新模块[下载即将开始]')
        if r == wx.ID_OK:
            self.Destroy()
        if r == wx.OK:
            print('任务开始，请回到聊天室聊天，稍后会提醒你...')
            LOG_OS.log_log(LOG_OS, '更新模块[用户确定开始]')
            dlg = wx.MessageDialog(self, '任务开始，请回到聊天室聊天，下载将在2-8分钟内完成,过程中将会出现未响应情况。进入下一流程会提醒你...', "任务开始", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.Up_main()
    def Version_checking(self):#版本检查
        print('[%s]连接版本服务器..\n' %(time.strftime("%F %H:%M:%S")))
        self.control.AppendText('[%s]连接版本服务器..\n' %(time.strftime("%F %H:%M:%S")))
        try:
            client = socket.socket()  # 生成socket连接对象
            ip_port = ("www.huoyinetwork.cn", 6979)  # 地址和端口号 填localhost可以进行本地测试
            client.connect(ip_port)  # 连接
        except:
            print("[%s]状态：连接服务器失败！3秒后退出..." %(time.strftime("%F %H:%M:%S")))
            self.control.AppendText('[%s]状态：连接服务器失败！3秒后退出...\n' %(time.strftime("%F %H:%M:%S")))
            time.sleep(3)
            exit()
        else:
            print("[%s]状态：服务器连接成功!" %(time.strftime("%F %H:%M:%S")))
            self.control.AppendText('[%s]状态：服务器连接成功!\n' %(time.strftime("%F %H:%M:%S")))
        bit = struct.calcsize("P") * 8
        content = ("Verg 1215")
        print('如果6秒内没有动静，可能是服务器被关闭。')
        self.control.AppendText('\n如果6秒内没有动静，可能是网络故障。\n')
        client.send(content.encode("utf-8"))  # 传送和接收都是bytes类型
        time.sleep(1)
        # 1.先接收长度，建议8192
        server_response = client.recv(1024)
        new_ver,gx_log,gx_nei = str(server_response).split('@')
        #new_ver = str(server_response.decode("utf-8"))
        client.close()
        return new_ver,gx_log,gx_nei
    def get_sss(self,size):
        # 2**10 = 1024
        power = 2 ** 10
        n = 0
        Dic_powerN = {0: '', 1: 'KB[较小资源]', 2: 'MB[普通文件]', 3: 'GB[较大文件]', 4: 'T[超大文件]'}
        while size > power:
            size /= power
            n += 1
        return ('%s%s' %(size, Dic_powerN[n]))
    def Up_main(self):
        self.control.AppendText('\n\n=============real-time information===============.\n')
        print('连接更新服务器...')
        self.control.AppendText('[%s]连接更新服务器..\n.' %time.strftime('%F %H:%M:%S'))
        try:
            client = socket.socket()  # 生成socket连接对象
            ip_port = ("www.huoyinetwork.cn", 6979)  # 地址和端口号 填localhost可以进行本地测试
            client.connect(ip_port)  # 连接
        except:
            print("状态：连接服务器失败！3秒后退出...")
            self.control.AppendText('[%s]状态：连接服务器失败！3秒后退出...\n' %time.strftime('%F %H:%M:%S'))
            time.sleep(3)
            exit()
        else:
            print("状态：服务器连接成功!")
            self.control.AppendText('[%s]状态：服务器连接成功!\n' %time.strftime('%F %H:%M:%S'))
        bit = struct.calcsize("P") * 8
        try:
            content = ("get pyinstallers%sbit.%s" % (bit, ver_nei))
        except:
            client.close() #关闭刚刚建立的连接，避免混乱。
            self.ver_sss(e=0)  #如果没有运行版本检查则执行
            content = ("get pyinstallers%sbit.%s" % (bit, ver_nei))
            self.control.AppendText('\n=============real-time information===============.\n')
            print('重新连接更新服务器...')
            self.control.AppendText('[%s]重新连接更新服务器..\n.' % time.strftime('%F %H:%M:%S'))
            try:
                client = socket.socket()  # 生成socket连接对象
                ip_port = ("www.huoyinetwork.cn", 6979)  # 地址和端口号 填localhost可以进行本地测试
                client.connect(ip_port)  # 连接
            except:
                print("状态：重新连接服务器失败！3秒后退出...")
                self.control.AppendText('[%s]状态：连接服务器失败！3秒后退出...\n' % time.strftime('%F %H:%M:%S'))
                time.sleep(3)
                exit()
            else:
                print("状态：重新服务器连接成功!")
                self.control.AppendText('[%s]状态：服务器连接成功!\n' % time.strftime('%F %H:%M:%S'))

        #content = ("get s01.wav")
        print(content)
        self.control.AppendText('[%s]下载任务：%s\n' %(time.strftime('%F %H:%M:%S'),content))
        client.send(content.encode("utf-8"))  # 传送和接收都是bytes类型

        # 1.先接收长度，建议8192
        server_response = client.recv(1024)
        file_size = int(server_response.decode("utf-8"))

        print("目标文件总大小：%s字节" % file_size)
        self.control.AppendText("[%s]目标文件总大小：%s字节\n" %(time.strftime('%F %H:%M:%S'),file_size))

        # 2.接收文件内容
        client.send("准备好接收".encode("utf-8"))  # 接收确认
        #filename = "new" + content.split(" ")[1]
        filename = content.split(" ")[1]

        f = open(filename, "wb")
        received_size = 0
        m = hashlib.md5()
        als = 0
        print('开始下载...')
        self.control.AppendText('[%s]开始下载...\n' %time.strftime('%F %H:%M:%S'))
        #--带进度条的下载进度窗口
        #app = wx.PySimpleApp()
        progressMax = 100
        file_size_g = str(self.get_sss(file_size))

        upstie = {'upini':'自调整更新','zip':'整体更新','txt':'文本更新','wav':'音频更新','exe':'整体更新'}
        neixing = upstie[ver_nei]
        dialog = wx.ProgressDialog("文件下载[%s]" %neixing, "更新文件总大小：%s" %file_size_g, progressMax,style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
        keepGoing = True
        count = 0
        #--窗口设置结束
        while received_size < file_size:
            size = 0  # 准确接收数据大小，解决粘包
            if file_size - received_size > 1024:  # 多次接收
                size = 1024
            else:  # 最后一次接收完毕
                size = file_size - received_size
            data = client.recv(size)  # 多次接收内容，接收大数据
            data_len = len(data)
            received_size += data_len
            aas = int(received_size / file_size * 100)
            if aas != als:  # 避免刷屏
                #print('█' * aas)
                print("已接收：", int(received_size / file_size * 100), "%")
                self.control.AppendText("[%s]已接收：" %time.strftime('%F %H:%M:%S') + str(aas) + "%\n")
                #进度条更新---
                count = count + 1
                #wx.Sleep(1)
                #进度条更新结束
                if aas == 100:
                    winsound.PlaySound("11250.wav", winsound.SND_ASYNC)
                keepGoing = dialog.Update(count)  # 更新进度条

            als = int(received_size / file_size * 100)
            m.update(data)
            f.write(data)
        print('最新版程序下载完成,正在校验文件...')
        self.control.AppendText("[%s]最新版程序下载完成,正在校验文件..\n" %time.strftime('%F %H:%M:%S'))
        #self.showDialog('提示：下载完成', '文件下载完成\n请手动安装最新版程序\n感谢有你.', (200, 100))  # 第一个是弹窗标题
        dialog.Destroy() #销毁窗口
        f.close()

        print("已经接收的大小:%s" % received_size)  # 解码
        self.control.AppendText("[%s]已经接收的大小:%s\n" %(time.strftime('%F %H:%M:%S'),received_size))

        # 3.md5值校验
        md5_sever = client.recv(1024).decode("utf-8")
        md5_client = m.hexdigest()
        print("服务器发来的md5:", md5_sever)
        print("接收文件的md5:", md5_client)
        if md5_sever == md5_client:
            print("MD5值校验成功")
            self.control.AppendText('检验完成：文件正确且完整！\n')
        else:
            print("MD5值校验失败")
            self.control.AppendText('检验完成：文件出现错误，我们将不会继续！\n')
        client.close()#关闭连接
        name,hou = filename.split('.')
        if hou == 'zip':
            path_now = os.getcwd()
            path = (r'%s' %path_now)
            print('整体更新(压缩包)，正在解压压缩包....')
            self.control.AppendText('[%s]整体更新，正在解压压缩包....\n' %time.strftime('%F %H:%M:%S'))
            zip_path = ("%s/pyinstallers%sbit.zip" % (path_now, bit))
            self.control.AppendText('[%s]压缩包路径:%s\n' %(time.strftime('%F %H:%M:%S'),zip_path))
            os.startfile(path)
            f = zipfile.ZipFile("%s/pyinstallers%sbit.zip" %(path_now,bit), 'r')
            #path_jieya = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir)) #解压至上一级目录
            path_jieya = path_now #解压至当前目录
            try:
                for file in f.namelist():
                    f.extract(file, path_jieya)
            except:
                print('[%s]Zip-jieya-Error:自动解压文件失败，请手动解压更新文件' %time.strftime('%F %H:%M:%S'))
            else:
                print('解压完成，软件已部署完成')
        elif hou == 'txt' or hou == 'wav' or hou == 'png' or hou == 'jpg':
            print('资源文件更新，将会覆盖源文件')
            self.control.AppendText('[%s]资源文件更新，将会覆盖源文件\n' %time.strftime('%F %H:%M:%S'))
        elif hou == 'exe':
            print('整体更新（安装包），正在准备安装新版本...')
            self.control.AppendText('[%s]整体更新（安装包），正在准备安装新版本...' %time.strftime('%F %H:%M:%S'))
            self.WriteRestartCmd("pyinstallers%sbit.exe" % bit)
            dlg = wx.MessageDialog(self, '[%s]任务执行完毕，但我们不确定安装包是否启动，如果5秒后安装包没用启动，请到安装目录下找到pyinstallers%sbit.exe并运行它' % (time.strftime('%F %H:%M:%S'),bit), "更新完成", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        elif hou == 'upini':
            print('分段更新（upini），准备执行upini文件...')
            self.control.AppendText('分段更新（upini），准备执行upini文件...\n')
            time.sleep(3)
            self.control.AppendText('执行失败：我们无法在本地找到upini指定的需更新项目，更新无法继续\n')

        print('更新完成！')
        self.control.AppendText('[%s]更新完成！\n====================\n' %time.strftime('%F %H:%M:%S'))
        winsound.PlaySound("11250.wav", winsound.SND_ASYNC)
        print(self.check1.GetLabel)
        if self.check1.GetLabel == True:
            print('您选择了自动重启，将会自动重启客户端')
            self.control.AppendText('[%s]您选择了自动重启，将会自动重启客户端。' %time.strftime('%F %H:%M:%S'))
            self.zdgx_main()  #自动删除及重启
        else:
            print('您没选择自动重启，请您手动重启客户端')
            self.control.AppendText('[%s]您没选择自动重启，请您手动重启客户端。' %time.strftime('%F %H:%M:%S'))
            dlg = wx.MessageDialog(self, '[%s]您没选择自动重启，请您手动重启客户端。' %time.strftime('%F %H:%M:%S'), "更新完成", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    MainFrame(None,-1,'Up_Module-软件版本更新及应急修复中心',(650,430))

    app.MainLoop()
else:
    app = wx.App()
    MainFrame(None, -1, 'Up_Module-软件版本更新及应急修复中心', (650, 430))

    app.MainLoop()