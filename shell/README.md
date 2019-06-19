# UPCDdnspod Shell Script

在中国石油大学（华东）校园网中使用 `DNSPod` 用户 `API` 实现的纯 `Shell` 动态域名客户端

## Usage

复制 `dns.conf.example` 到同一目录下的 `dns.conf` 并根据你的配置修改即可。

执行时直接运行 `ddnspod.sh`，支持 `cron` 任务。

配置文件格式：

```
# 安全起见，不推荐使用密码认证
# arMail="test@gmail.com"
# arPass="123"

# 推荐使用Token认证
# 按`TokenID,Token`格式填写
arToken="12345,7676f344eaeaea9074c123451234512d"

# 每行一个域名
arDdnsCheck "test.org" "subdomain"
```

## Credit

+ From: [ArDNSPod](https://github.com/anrip/ArDNSPod)
