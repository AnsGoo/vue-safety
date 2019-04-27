#!/usr/bin/python
#coding:utf-8

'''
堡垒机菜单入口
'''

import os
import sys
import readline
import MySQLdb
import getpass

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def con(host,user,passwd,db,sql):
    # 打开数据库连接
    db = MySQLdb.connect(host, user, passwd, db, charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return data


host = '192.168.1.218'
user = 'root'
passwd = 'mysql'
db = 'mtrops'
sql_host= "select a.IP,a.port,a.msg from app_cmdb_hostinfo a where  a.os_type='Linux';"
sql_user = "select login_user,login_passwd,private_key from app_cmdb_loginuser where login_user='%s';" % getpass.getuser()
hostinfo = con(host, user, passwd, db, sql_host)

userinfo = con(host, user, passwd, db, sql_user)

try:
    user = userinfo[0]
except:
    pass

host_list = []
for i in hostinfo:

    host_info = {'ip': i[0], 'hostname': i[2], 'port': i[1],'username': user[0],
                 'passwd': user[1], 'private_key': user[2]}
    host_list.append(host_info)



usege_msg = '''\033[1;32m
================================================================================================
                            Welcome using mtrops bastion system!
    Quit: Use ":q<Enter>".

 Connect: Select a Number to connect to the remote host
================================================================================================
\033[0m'''


head_num = "Number"
head_ip = "IP"
head_hostname = "HostName"

head_msg = "\033[1;34m %-10s%-20s%-50s\033[0m" % (head_num, head_ip, head_hostname)

while True:
    print (usege_msg)
    print (head_msg)
    n = 1
    host_dict = {}
    for host in host_list:
        if n<10:
            num = "0%d" % n
        else:
            num = str(n)
        msg = "\033[1;36m %-10s%-20s%-50s\033[0m" % (num, host['ip'], host['hostname'])
        print (msg)
        host_dict[num] = host
        n+=1

    print("\000")
    try:
        num = raw_input('\033[1;35mPlease choose one host to login:\033[0m').strip()
        if num == 'q':
            print ('\033[1;32m Goodbye ! \033[0m')
            os.system("exit")
            break
    except:
        continue

    if len(num) == 0:
        continue

    if not num in host_dict:
        msg = """\033[1;31m
No host matched,try again or input q to exit!\033[0m
"""
        print (msg)
        continue

    print ('\033[32;1mGoing to connect %s \033[0m' % host_dict[num]['ip'])
    host_info = host_dict[num]

    hostname = host_info['ip']
    port = host_info['port']
    username = host_info['username']
    passwd = host_info['passwd']
    private_key = host_info['private_key']

    if private_key:
        if os.path.exists("/tmp/%s/" % username):
            pass
        else:
            os.mkdir("/tmp/%s/" % username)

        key_file = open("/tmp/%s/%s_%s" % (username,hostname, username), 'w')
        key_file.write(private_key)
        key_file.close()
        key_path = "/tmp/%s/%s_%s" % (username,hostname, username)

        os.system("chmod 600 %s" % key_path)
        ssh_con = "ssh %s@%s -p %s -i %s" % (username, hostname, port, key_path)
    else:
        ssh_con = "sshpass -p %s ssh %s@%s -p %s" % (passwd, username, hostname, port)
    os.system(ssh_con)