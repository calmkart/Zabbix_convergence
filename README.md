# Zabbix_convergence
一个简单的Zabbix报警收敛程序     

convergence.py脚本作为server端，接收client端发来的zabbix报警数据，同时做收敛处理          

client端通过TCP SOCKET连接到SERVER端，给SERVER端发送模拟的ZABBIX报警数据
