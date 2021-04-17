#coding=utf-8
# 服务器端

import socket
import os
import hashlib
import time
import configparser

print('Loading for config...')
global port
global ver
global newconfig
config = configparser.ConfigParser()
re = config.read('config-pyinatll.ini')
if os.path.isfile('config-pyinatll.ini'):
    #读取配置信息
    port = config.get('mianban', option='port')#端口
    ver = config.get('mianban', option='ver')#最新版本
    newconfig = config.get('mianban',option='newconfig')#最新版本提醒配置（描述、大小、下载地址）
    
else:
    print('读取配置文件失败，5s后终止程序')
    time.sleep(5)
    exit()

server = socket.socket()
server.bind(("", port)) # 绑定监听端口 填localhost可以进行本地测试
server.listen(5)  # 监听

print("监听开始..")

while True:
    conn, addr = server.accept()  # 等待连接

    print("conn:", conn, "\naddr:", addr)  # conn连接实例

    while True:
        try:
            data = conn.recv(1024)  # 接收
            if not data:  # 客户端已断开
                print(time.strftime('[%F %H:%M:%S]'),"客户端断开连接")
                break
        except:
            print('客户端异常断开连接！')
            break

        print(time.strftime('[%F %H:%M:%S]'),"收到的命令：", data.decode("utf-8"))
        #if data.startswith("HTTP"):  # 判断是否是浏览器直接访问
        #    print("该IP直接通过浏览器访问，开始引导...")
        #    break
        #    #conn.send('<a href="http://www.huoyifpa.top/static/HO/fpaup32bit.zip">下载客户端</a>')
        try:
            cmd, filename = data.decode("utf-8").split(" ")
        except:
            print('该IP直接通过浏览器访问，发送引导信息。。。')
            wenl = ('This server is only for software system calls. Please copy the following link to the browser to download the software.\nhttp://www.huoyifpa.top/static/HO/fpaup32bit.zip').encode('utf-8')
            conn.send(wenl)
            break
        if cmd =="get":
            if os.path.isfile(filename):  # 判断文件存在

                # 1.先发送文件大小，让客户端准备接收
                size = os.stat(filename).st_size  #获取文件大小
                conn.send(str(size).encode("utf-8"))  # 发送数据长度
                print(time.strftime('[%F %H:%M:%S]'),"发送的大小：", size)

                # 2.发送文件内容
                conn.recv(1024)  # 接收确认

                m = hashlib.md5()
                print(time.strftime('[%F %H:%M:%S]'),'读取数据...')
                f = open(filename, "rb")
                print(time.strftime('[%F %H:%M:%S]'),'发送数据...')
                q = 0
                for line in f:
                    try:
                        conn.send(line)  # 发送数据
                        m.update(line)
                        q+=1
                    except:
                        print(time.strftime('[%F %H:%M:%S]'),'客户端异常断开连接！')
                        break
                f.close()
                print('切片次数：',q)

                # 3.发送md5值进行校验
                md5 = m.hexdigest()
                try:
                    conn.send(md5.encode("utf-8"))  # 发送md5值
                except:
                    print(time.strftime('[%F %H:%M:%S]'),'客户端异常断开连接！')
                print("md5:", md5)
                print(time.strftime('[%F %H:%M:%S]'),'[%s]发送完成！！' % filename)
            else:
                print(time.strftime('[%F %H:%M:%S]'),'【%s】文件不存在' %filename)
                #conn.send(time.strftime('[%F %H:%M:%S]'),'【%s】文件不存在' %filename)
        elif cmd == 'Verg':
                print('客户端请求版本检查')
                #版本检查及更新类型确定
                verg = ('%s@%s' %(vew,newconfig))  # 最新版本号（公）、更新记录及版本说明，以@作为分隔符
                conn.send(str(verg).encode("utf-8"))
                break
        elif cmd == "Exit":
            if filename == 'Administrator-1927767':
                print(time.strftime('[%F %H:%M:%S]'),'超级管理员远程指令【关闭程序】，立刻执行')
                server.close()
                exit()

server.close()

