#!/usr/bin/env python3
import requests
import json

config = None


def get_domain_id(domain, login_token):
    json_response = requests.api.post('https://dnsapi.cn/Domain.List', data={
        'login_token': login_token,
        'format': 'json'
    }).json()
    for detail in json_response['domains']:
        if detail['name'] == domain:
            return detail['id']

    print("get domain_id error")
    exit(0)


def get_record_id(record, domain_id, login_token):
    json_response = requests.api.post('https://dnsapi.cn/Record.List', data={
        'login_token': login_token,
        'format': 'json',
        'domain_id': domain_id
    }).json()
    for detail in json_response['records']:
        if detail['name'] == record:
            return detail['id']

    print('get record_id error')
    exit(0)


def init(sub_domain, domain, login_token):
    global config
    domain_id = get_domain_id(domain, login_token)
    record_id = get_record_id(sub_domain, domain_id, login_token)
    config['record_id'] = str(record_id)
    config['domain_id'] = str(domain_id)
    with open("config.json", "w") as file:
        json.dump(obj=config, fp=file, indent=4)


if __name__ == '__main__':
    with open("config.json") as file:
        config = json.load(file)

    init(config['sub_domain'], config['domain'], '%s,%s' % (config['ID'], config['token']))
