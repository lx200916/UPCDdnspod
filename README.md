# ddns

将本地的 IP 推至 DNSPOD

# 指南

```json
{
    "ID": 12345,
    "token": "abcdefghijklmnopqrstuvwxyz123456",
    "domain_id": 12345678,
    "record_id": 123456789,
    "sub_domain": "www",
    "ip_current": "127.0.0.1"
}
```

其中：

1. `ID` 为 [DNSPOD / 用户中心 / 安全设置 / API Token](https://www.dnspod.cn/console/user/security) 中的 `ID`
2. `token` 为上述 `API Token` 页面中的 `token`
3. `domain_id` 通过 `curl -X POST https://dnsapi.cn/Domain.List -d 'login_token=LOGIN_TOKEN&format=json'` 获得
4. `record_id` 通过 `curl -X POST https://dnsapi.cn/Record.List -d 'login_token=LOGIN_TOKEN&format=json&domain_id=xxx'`
5. `sub_domain` 就是你要动态更新的子域名，详见获取 `record_id` 时从官网得到的 `json` 中的 `name` 参数
6. `ip_current` 由程序来修改，这里只是起到一个超微型数据库的作用

详见：https://www.lucien.ink/archives/396/

# 鸣谢

[@Andyliu](https://github.com/andyliu24)
