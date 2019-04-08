import os
import json

config = None


def request(cmd):
    os.system(cmd + ' > buf')
    with open('buf') as file:
        json_response = json.load(file)
    os.system('rm buf')
    return json_response


def get_domain_id(domain, login_token):
    json_response = request("curl 'https://dnsapi.cn/Domain.List' -d 'login_token=%s&format=json'" % login_token)
    for detail in json_response['domains']:
        if detail['name'] == domain:
            return detail['id']

    print("get domain_id error")
    exit(0)


def get_record_id(domain_id, record, login_token):
    json_response = request("curl 'https://dnsapi.cn/Record.List' -d "
                            "'login_token=%s&format=json&domain_id=%s'" % (login_token, domain_id))
    for detail in json_response['records']:
        if detail['name'] == record:
            return detail['id']

    print('get record_id error')
    exit(0)


def init(sub_domain, domain, login_token):
    global config
    domain_id = get_domain_id(domain, login_token)
    record_id = get_record_id(domain_id, sub_domain, login_token)
    config['record_id'] = str(record_id)
    config['domain_id'] = str(domain_id)
    with open("config.json", "w") as file:
        json.dump(obj=config, fp=file, indent=4)


if __name__ == '__main__':
    with open("config.json") as file:
        config = json.load(file)

    init(config['sub_domain'], config['domain'], '%s,%s' % (config['ID'], config['token']))
    
