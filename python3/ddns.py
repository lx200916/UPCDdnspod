#!/usr/bin/env python3
import time
import requests
import json
import os

path = os.path.split(os.path.realpath(__file__))[0] + os.path.sep  # 脚本根目录


def logger(level, message):
    with open(path + "log.txt", "a") as file:
        file.write("%s %s: %s\n" % (
            "[INFO]" if level == 0 else "[WARN]",
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            message))
        print("%s %s" % ("[INFO]" if level == 0 else "[ERROR]", message))
    if level == -1:
        exit(-1)


def config_reader():
    if os.path.exists(path + "config.json"):
        try:
            with open(path + "config.json", "r") as file:
                config = json.load(file)
                return config
        except Exception as exception:
            logger(-1, repr(exception))

    logger(-1, "`config.json` not found")


def config_writer(config):
    try:
        with open(path + "config.json", "w") as file:
            file.write(json.dumps(config, indent=4))
            logger(0, "IP updated: %s" % config['ip_current'])
    except Exception as exception:
        logger(-1, repr(exception))


def get_domain_id(domain, login_token):
    json_response = requests.api.post('https://dnsapi.cn/Domain.List', data={
        'login_token': login_token,
        'format': 'json'
    }).json()
    for detail in json_response['domains']:
        if detail['name'] == domain:
            return detail['id']

    logger(-1, "get domain_id error")


def get_record_id(record, domain_id, login_token):
    json_response = requests.api.post('https://dnsapi.cn/Record.List', data={
        'login_token': login_token,
        'format': 'json',
        'domain_id': domain_id
    }).json()
    for detail in json_response['records']:
        if detail['name'] == record:
            return detail['id']

    logger(-1, 'get record_id error')


def update(config):
    login_token = "%s,%s" % (config['ID'], config['token'])
    domain_id = get_domain_id(config['domain'], login_token)
    record_id = get_record_id(config['sub_domain'], domain_id, login_token)
    return request_dnspod(login_token, config['sub_domain'], domain_id, record_id, config['ip_current'])


def request_dnspod(login_token, sub_domain, domain_id, record_id, ip):
    json_response = requests.api.post('https://dnsapi.cn/Record.Ddns', data={
        'login_token': login_token,
        'format': 'json',
        'sub_domain': sub_domain,
        'domain_id': domain_id,
        'record_id': record_id,
        'record_line': "默认",
        'value': ip
    }).json()
    message = json_response['status']['message']
    logger(0, "Message from DNSPOD: " + message)
    return message == "Action completed successful"


def get_ip():
    # address = "http://lan.upc.edu.cn/eportal/InterFace.do?method=getOnlineUserInfo"  # 有线
    # address = "http://wlan.upc.edu.cn/eportal/InterFace.do?method=getOnlineUserInfo"  #无线
    # return requests.api.get(address).json()['userIp']
    return requests.api.get('https://ifconfig.co/ip').content.decode('utf-8').strip()


if __name__ == '__main__':
    try:
        config = config_reader()
        logger(0, "IP from `config.json`: %s" % config['ip_current'])
        ip_eportal = get_ip()
        logger(0, "IP from ePortal: " + ip_eportal)
        if config['ip_current'] != ip_eportal:
            config['ip_current'] = ip_eportal
            if update(config):
                config_writer(config)
            else:
                logger(-1, "Something Wrong, please see the log.txt file at: %s" % path + "log.txt")
        else:
            logger(0, "Nothing different with IP from `config.json` and ePortal")
    except Exception as exception:
        logger(-1, repr(exception))
