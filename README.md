# ddns

将本地的 IP 推至 DNSPOD

# 指南

```json
{
    "ID": "12345",
    "token": "abcdefghijklmnopqrstuvwxyz123456",
    "domain_id": "",
    "record_id": "",
    "sub_domain": "www",
    "domain": "example.com",
    "ip_current": "127.0.0.1"
}
```

其中：

1. `ID` 为 [DNSPOD / 用户中心 / 安全设置 / API Token](https://www.dnspod.cn/console/user/security) 中的 `ID`
2. `token` 为上述 `API Token` 页面中的 `token`
3. `sub_domain` 就是你要动态更新的子域名
4. `domain` 是你的域名主体部分

完善上述四项之后，执行 `python3 init.py` 来进行初始化

5. `ip_current` 由程序来修改，这里只是起到一个超微型数据库的作用，用户忽略即可

手动获取 `domain_id` 和 `record_id`：

1. `domain_id` 通过 `curl -X POST https://dnsapi.cn/Domain.List -d 'login_token=LOGIN_TOKEN&format=json'` 获得
2. `record_id` 通过 `curl -X POST https://dnsapi.cn/Record.List -d 'login_token=LOGIN_TOKEN&format=json&domain_id=xxx'`

详见：https://www.lucien.ink/archives/396/

# 其它

默认适用于获取 UPC 校内的 `IP` ，获取公网 `IP` 需 `import sock` ，然后将下面的函数替换源码中 `get_ip()` 函数：

```python
def get_ip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666), 20)
    ip = sock.recv(16)
    sock.close()
    return ip
```

# 鸣谢

[@Andy Liu](https://github.com/andyliu24)
