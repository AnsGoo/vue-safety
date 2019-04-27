#!/usr/bin/python
# coding:utf-8


#ceshi,test

import re
import os
import time
import MySQLdb
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

sql_host = '192.168.1.218'
sql_user = 'root'
sql_passwd = 'mysql'
sql_db = 'mtrops'


def con(host, user, passwd, db, sql):
    # 打开数据库连接
    db = MySQLdb.connect(host, user, passwd, db, charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()

    db.commit()
    # 关闭数据库连接
    db.close()
    return data


def upload_log(log_file):
    f = open(log_file, 'r')
    data = f.read()
    result_list = re.findall("Going(.*?)======================", data, re.S)
    path_list = log_file.split('/')
    user = path_list[3]
    tm_hour = path_list[-1].strip('.log')
    tm_date = "-".join(path_list[4:-1])
    tm_str = tm_date + ' ' + tm_hour
    t = time.strptime(tm_str, '%Y-%m-%d %H%M%S')
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", t)

    for i in result_list:
        ip = re.findall("to connect (.*?)\n", i, re.S)[0]
        ip = re.match(r"\d+.\d+.\d+.\d+", ip).group()
        text = re.sub(" to connect .*", "", i)
        a = re.sub(r"\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]", '', text)

        b = re.sub("\x1b]0;.*\x07", '', a)

        b = re.sub("\"\x08\r\n", "\"\r\n", b)

        b = re.sub("\x1b\[1P", '', b)
        b = re.sub("\"\x08", '', b)
        b = re.sub("\x08", '', b)

        b = re.sub(r"\x1b\[H\x1b\[2J", r'\r\n', b)

        c = re.sub(r"\x1b\[\?1034h", '', b)

        d = re.sub("'", r"\'", c)
        e = re.sub('"', r'\"', d)

        sql_select_hostname = "select msg from app_cmdb_hostinfo where ip='%s'" % ip
        hostname = con(sql_host, sql_user, sql_passwd, sql_db, sql_select_hostname)[0][0]
        sql_insert = "INSERT INTO app_log_audit(hostname,host_ip,user_name,start_time,audit_log) VALUES('%s','%s','%s','%s','%s')" % (
            hostname, ip, user, time_str, d)
        con(sql_host, sql_user, sql_passwd, sql_db, sql_insert)


if __name__ == "__main__":
    log_file = sys.argv[1]
    upload_log(log_file)
