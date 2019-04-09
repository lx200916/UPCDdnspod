# ddns

将本地的 IP 推至 DNSPOD

# Requirements

```bash
python3.6+
requests
json
os
time
```

# 指南

```json
{
    "ID": "12345",
    "token": "abcdefghijklmnopqrstuvwxyz123456",
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
5. `ip_current` 由程序来修改，这里只是起到一个超微型数据库的作用，用户忽略即可

详见：https://www.lucien.ink/archives/396/

# 其它

默认适用于获取 UPC 校内的 `IP` ，获取公网 `IP` 需 `import socket` ，然后将下面的函数替换源码中 `get_ip()` 函数：

```python
def get_ip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666), 20)
    ip = sock.recv(16)
    sock.close()
    return ip
```

# 鸣谢

[@Andy Liu](https://github.com/andyliu24)
