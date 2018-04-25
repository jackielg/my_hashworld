# coding=utf-8

import json
import logging
import os
import re
import ssl
import time

import requests
import schedule

import Send_email

# 日志
# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
logfile = 'new.log'
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.WARNING)  # 输出到file的log等级的开关

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
# 第四步，将logger添加到handler里面
logger.addHandler(fh)

ch.setFormatter(formatter)
logger.addHandler(ch)

# logger.debug('this is a logger debug message')
# logger.info('this is a logger info message')
# logger.warning('this is a logger warning message')
# logger.error('this is a logger error message')
# logger.critical('this is a logger critical message')

# start
logging.warning('Start ...')
curpath = os.getcwd()

# get config information
content = open(curpath + '/config.ini').read()
content = re.sub(r"\xfe\xff", "", content)
content = re.sub(r"\xff\xfe", "", content)
content = re.sub(r"\xef\xbb\xbf", "", content)
open(curpath + '\config.ini', 'w').write(content)


def open_FirstPage():
    url = "https://game.hashworld.top/"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/plain, */*",
        'user-agent': "Mozilla/5.0 (Linux; Android 4.4.2; ZTE Q2S-T Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
        'accept-language': "zh-CN,zh;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'cache-control': "no-cache"
    }

    try:
        requests.packages.urllib3.disable_warnings()
        ssl._create_default_https_context = ssl._create_unverified_context
        time.sleep(1)
        response = requests.request("GET", url, headers=headers, verify=False)
        res = response.status_code
        logging.warning('********** open_FirstPage(), status_code=' + str(res))

        if res == 200:
            return res
        else:
            return -1
    except Exception as e:
        print(e)
        return -1


def login_GetAccessToken(payload):
    url = "https://game.hashworld.top/apis/accounts/token/"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/plain, */*",
        'user-agent': "Mozilla/5.0 (Linux; Android 4.4.2; ZTE Q2S-T Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
        'accept-language': "zh-CN,zh;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'cache-control': "no-cache"
    }

    try:
        requests.packages.urllib3.disable_warnings()
        ssl._create_default_https_context = ssl._create_unverified_context
        time.sleep(1)
        response = requests.request("POST", url, data=payload, headers=headers)

        res = response.json()["status"]
        if res == 'common_OK':
            token = response.json()["data"]["token"]
            return token
        else:
            return -1
    except Exception as e:
        print(e)
        return -1


def get_prize_wheel(token):
    url = "https://game.hashworld.top/apis/game/prize_wheel/"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/plain, */*",
        'user-agent': "Mozilla/5.0 (Linux; Android 4.4.2; ZTE Q2S-T Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
        'accept-language': "zh-CN,zh;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'authorization': "Token " + token,
        'cache-control': "no-cache"
    }

    try:
        requests.packages.urllib3.disable_warnings()
        ssl._create_default_https_context = ssl._create_unverified_context
        time.sleep(1)
        response = requests.request("GET", url, headers=headers)

        res = response.json()["status"]
        if res == 'common_OK':
            wonder_list = response.json()['data']
            return wonder_list
    except Exception as e:
        print(e)
        return -1


def click_Lottery(token, block_number):
    url = "https://game.hashworld.top/apis/game/lottery/"

    headers = {
        'user-agent': "application/x-www-form-urlencoded",
        'accept-language': "zh-CN,zh;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'authorization': "Token " + token,
        'content-type': "application/json",
        'cache-control': "no-cache"
    }

    try:
        payload = "{\n\t\"block_number\": " + str(block_number) + "\n}"

        requests.packages.urllib3.disable_warnings()
        ssl._create_default_https_context = ssl._create_unverified_context
        time.sleep(1)
        response = requests.request("PUT", url, data=payload, headers=headers)

        res = response.json()["status"]
        if res == 'common_OK':
            coin_name = response.json()["data"]["coin_name"]
            logging.warning('>>>>>>>>>> lottery...... ' + coin_name)
            return 0
        else:
            return -1
    except Exception as e:
        print(e)
        return -1


def check_UserTotal(token):
    url = "https://game.hashworld.top/apis/coin/gift_wallet/"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/plain, */*",
        'user-agent': "Mozilla/5.0 (Linux; Android 4.4.2; ZTE Q2S-T Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
        'accept-language': "zh-CN,zh;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'authorization': "Token " + token,
        'cache-control': "no-cache"
    }

    total = 0

    try:
        requests.packages.urllib3.disable_warnings()
        ssl._create_default_https_context = ssl._create_unverified_context
        time.sleep(1)
        response = requests.request("GET", url, headers=headers)

        res = response.json()["status"]
        if res == 'common_OK':
            totallist = response.json()['data']
            for i in range(len(totallist)):
                market_price_cny = totallist[i]['coin']['market_price_cny']
                active_balance = totallist[i]['active_balance']
                total = total + market_price_cny * active_balance
            logging.warning('>>>>>>>>>> Total: ' + str(total))
            return total
        else:
            return -1
    except Exception as e:
        print(e)
        return -1


def loop_Lottery():
    all_total = 0
    content_list = []

    file = open('hash_world_data.json', 'r', encoding='utf-8')
    data_dict = json.load(file)
    # print(data_dict)
    # print(type(data_dict))

    for item in data_dict['data']:
        phone = item.get('phone', 'NA')
        password = item.get('password', 'NA')
        data = dict(phone=phone, password=password)
        logging.warning("========== Checking [" + phone + "] ==========")

        token = login_GetAccessToken(data)
        if token == -1:
            logging.warning('********** Login fail!')
            continue
        else:
            logging.warning('********** Login success! token:' + token)

            wonder_list = get_prize_wheel(token)
            if wonder_list == -1:
                continue

            reveal = 0
            for i in range(len(wonder_list)):
                has_reveal = wonder_list[i]['has_reveal']
                if bool(has_reveal):
                    reveal = reveal + 1
            logging.warning('********** Has revealed: ' + str(reveal))

            for j in range(len(wonder_list)):
                if reveal > 2:
                    break
                has_reveal = wonder_list[j]['has_reveal']
                if not bool(has_reveal):
                    # logging.warning('********** lottery_click')
                    lottery = click_Lottery(token, j)
                    if lottery == -1:
                        continue
                    else:
                        reveal = reveal + 1

            value = check_UserTotal(token)
            all_total = all_total + value
            logging.warning("========== End[" + phone + "], Total[ " + str(all_total) + " ] ==========")
            logging.warning('\n')

            # 构建Json数组，用于发送HTML邮件
            # Python 字典类型转换为 JSON 对象
            content_data = {
                "phone": phone,
                "value": value
            }
            content_list.append(content_data)
            time.sleep(2)
            # break

    # sending email
    Send_email.send_HtmlEmail('newseeing@163.com', content_list)
    logging.warning('********** Sending Email Complete!')
    logging.warning('\n')


def daily_job():
    status_code = open_FirstPage()
    while status_code != 200:
        time.sleep(300)
        status_code = open_FirstPage()
    loop_Lottery()


# Start from here...
daily_job()

# schedule.every(120).minutes.do(daily_job)
schedule.every(8).hours.do(daily_job)
# schedule.every().day.at("18:30").do(daily_job)
# schedule.every().monday.do(daily_job)
# schedule.every().wednesday.at("13:15").do(daily_job)

while True:
    schedule.run_pending()
    time.sleep(1)
