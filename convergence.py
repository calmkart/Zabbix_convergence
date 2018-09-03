# -*- coding:utf-8 -*-
from threading import Timer
import urllib2
import socket
import threading
import re

# event_list为收敛类型数目列表
# ip_list为IP收敛字典列表
# summary为收敛类型说明列表
# keyw为正则匹配元素


class convergence(object):
    event_list = [0, 0, 0, 0]
    summary = ['获取uptime时间失败',
               'SNMP_cant_respond_for_5minutes错误', 'OK错误', '流量速率异常错误']
    ip_list = [{}, {}, {}, {}]
    keyw = ['获取uptime时间失败', 'SNMPcan\'trespondfor5minutes', 'ok', '流量速度异常']
    t = None

    def convergence(self, event):
        temp = self.keyword(event)
        ip = self.findip(event)
        if temp != 0:
            # 做报警IP收敛
            if self.ip_list[temp-1].has_key(ip):
                self.ip_list[temp-1][ip] = self.ip_list[temp-1][ip]+1
            else:
                self.ip_list[temp-1][ip] = 1
            # 做报警条目收敛
            self.event_list[temp-1] = self.event_list[temp-1]+1
            if self.t == None:
                self.timer(event)
            else:
                pass

        else:
            # 按原格式发送
            print event
            pass

    def send(self, event):
        print '目前的缓存区为'+str(self.event_list)
        if max(self.event_list) == 0:
            pass
        else:
            for i in range(0, len(event_list)):
                if self.event_list[i] == 0:
                    pass
                else:  # 发送收敛后的报警到指定位置
                    content = str(event_list[i]+'次'+self.summary[i]+'(前20秒内)')
                    self.event_list[i] = 0
                    self.t = None
                    urllib2.urlopen('http://www.calmkart.com')
                    print content

    def timer(self, event):  # 启动定时器
        self.t = Timer(20, self.send, args=[event])
        self.t.start()

    def keyword(self, event):
        for i in range(0, len(self.keyw)):
            if re.search(self.keyw[i], event, flags=re.IGNORECASE) != None:
                return i+1
        return 0

    def findip(self, event):
        m = re.search(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', event)
        if m is not None:
            ip = m.group()
            return str(ip)
        return '查不到IP'


test = convergence()

# tcp测试,server端，接收
host = '0.0.0.0'
port = 9001
s = socket.socket()
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    test.convergence(data)

# udp测试,server端，接收
#s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#host = '10.17.16.207'
#port = 9001
# s.bind((host,port))
#
# while True:
#   data,addr = s.recvfrom(2048)
#   test.convergence(data)
