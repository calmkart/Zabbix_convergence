# --- coding:utf-8 ---
import random
from multiprocessing.connection import Client

str1 = [
	'192.168.0.1SNMP错误',
    '192.168.0.2SNMP错误',
    '192.168.0.100,OK',
    '192.168.0.101,ok',
	'192.168.0.102,流量速率异常',
	'192.168.0.103,流量速率异常',
	'192.168.0.104,获取uptime时间失败',
	'192.168.0.105,获取uptime时间失败',
] 
address = ('0.0.0.0',9001)

for i in range(0,1000):
	m = str1[random.randrange(0,11)]
	conn = Client(address)
	conn.send(m)
	conn.close