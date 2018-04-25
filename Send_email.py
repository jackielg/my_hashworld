#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import smtplib
import time
from email.mime.text import MIMEText

mailto_list = ['']  # 收件人(列表)
mail_host = "smtp.163.com"  # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user = "newseeing"  # 用户名
mail_pass = "Liuxb0504$"  # 密码
mail_postfix = "163.com"  # 邮箱的后缀，网易就是163.com


def send_mail(to_list, sub, content):
    me = "newseeing@163.com"
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = "newseeing@163.com"
    # msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # 连接服务器
        server.login(mail_user, mail_pass)  # 登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(e)
        return False


def send_HtmlEmail(to_list, content_list):
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    head = '<!DOCTYPE HTML>' + \
           '<html id="pageLoading">' + \
           '<head>' + \
           '<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>' + \
           '<title></title>' + \
           '<style type="text/css">' + \
           '/* Table Head */' + \
           '#table-7 thead th {' + \
           'background-color: rgb(81, 130, 187);' + \
           'color: #fff;' + \
           'border-bottom-width: 1;' + \
           '}' + \
           '/* Column Style */' + \
           '#table-7' + \
           'td {' + \
           'color: #000;' + \
           '}' + \
           '/* Heading and Column Style */' + \
           '#table-7 tr, #table-7 th {' + \
           'border-width: 1px;' + \
           'border-style: solid;' + \
           'border-color: rgb(0, 0, 0);' + \
           '}' + \
           '/* Padding and font style */' + \
           '#table-7 td, #table-7 th {' + \
           'padding: 5px 10px;' + \
           'font-size: 12px;' + \
           'font-family: Verdana;' + \
           'font-weight: bold;' + \
           '}' + \
           '</style>' + \
           '</head>' + \
           '<body>' + \
           '<p> ********** ' + datetime + ' ********** </p>' + \
           '<table border="1px" cellspacing="0px" style="border-collapse:collapse" id="table-7">' + \
           '<thead>' + \
           '<th align="center">No.</th>' + \
           '<th align="center">phone</th>' + \
           '<th align="center">value</th>' + \
           '</thead>' + \
           '<tbody>'

    end = '</tbody>' + \
          '</table>' + \
          '</body>' + \
          ' </html>'

    body = ''
    value_total = 0
    i = 0
    for item in content_list:
        i = i + 1
        phone = item.get('phone', 'NA')
        value = item.get('value', 'NA')
        value_total = value_total + value

        body = body + '<tr><td align="center">' + str(i) + \
               '</td><td align="center">' + phone + \
               '</td><td align="right">' + str(round(value, 2)) + '</td></tr>'
    sum = body + '<tr><td colspan="2" align="center">Sum:</td><td align="right">' + \
          str(round(value_total, 2)) + '</td></tr>'
    mail_msg = head + sum + end

    subject = "HashWorld, [Value:" + str(round(value_total, 2)) + "]"

    msg = MIMEText(mail_msg, 'html', 'utf-8')
    me = "newseeing@163.com"
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = "newseeing@163.com"
    # msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # 连接服务器
        server.login(mail_user, mail_pass)  # 登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(e)
        return False


def send_LandEmail(to_list, content_list):
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    head = '<!DOCTYPE HTML>' + \
           '<html id="pageLoading">' + \
           '<head>' + \
           '<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>' + \
           '<title></title>' + \
           '<style type="text/css">' + \
           '/* Table Head */' + \
           '#table-7 thead th {' + \
           'background-color: rgb(179, 103, 48);' + \
           'color: #fff;' + \
           'border-bottom-width: 1;' + \
           '}' + \
           '/* Column Style */' + \
           '#table-7' + \
           'td {' + \
           'color: #000;' + \
           '}' + \
           '/* Heading and Column Style */' + \
           '#table-7 tr, #table-7 th {' + \
           'border-width: 1px;' + \
           'border-style: solid;' + \
           'border-color: rgb(0, 0, 0);' + \
           '}' + \
           '/* Padding and font style */' + \
           '#table-7 td, #table-7 th {' + \
           'padding: 5px 10px;' + \
           'font-size: 12px;' + \
           'font-family: Verdana;' + \
           'font-weight: bold;' + \
           '}' + \
           '</style>' + \
           '</head>' + \
           '<body>' + \
           '<p> ********** ' + datetime + ' ********** </p>' + \
           '<table border="1px" cellspacing="0px" style="border-collapse:collapse" id="table-7">' + \
           '<thead>' + \
           '<th align="center">No.</th>' + \
           '<th align="center">Land_Num</th>' + \
           '<th align="center">Land_Name</th>' + \
           '<th align="center">Price</th>' + \
           '<th align="center">tradable_status</th>' + \
           '<th align="center">gen_time</th>' + \
           '</thead>' + \
           '<tbody>'

    end = '</tbody>' + \
          '</table>' + \
          '</body>' + \
          ' </html>'

    body = ''

    i = 0
    for item in content_list:
        i = i + 1
        land_num = item.get('land_num', 'NA')
        land_name = item.get('land_name', 'NA')
        price = item.get('price', 'NA')
        tradable_status = item.get('tradable_status', 'NA')
        gen_time = item.get('gen_time', 'NA')

        body = body + '<tr><td align="center">' + str(i) + \
               '</td><td align="center">' + str(land_num) + \
               '</td><td align="center">' + land_name + \
               '</td><td align="right">' + str(price) + \
               '</td><td align="center">' + tradable_status + \
               '</td><td align="center">' + gen_time + \
               '</td></tr>'
    sum = body + '<tr><td colspan="2" align="center">Sum:</td><td align="right"></td><td></td><td></td><td></td></tr>'
    mail_msg = head + sum + end

    # subject = "HashWorld, [Value:" + str(round(value_total, 2)) + "]"
    subject = "HashWorld, [Total Land: " + str(i) + "]"

    msg = MIMEText(mail_msg, 'html', 'utf-8')
    me = "newseeing@163.com"
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = "newseeing@163.com"
    # msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # 连接服务器
        server.login(mail_user, mail_pass)  # 登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(e)
        return False
