# bjut_ipv6
北京工业大学服务器ipv6免流量上网

Sina @偏不写作业
Github xbw12138
CSDN xbw12138
## 服务器版本
Ubuntu 16.04.4 LTS (GNU/Linux 4.15.0-36-generic x86_64)

## 问题
校园网流量不够用，使用ipv6免流量上网

## 解决方案
kcptun + ss + proxychains

## 目录介绍
### config为配置文件，包含kcptun配置文件，ss配置文件 
#### kcptun.json
此配置文件直接在使用kcptun加速的vps上获取，我们这里使用vps服务器的ipv6地址，
本地代理端口为1086，需要与ss本地端口匹配，与proxychains代理端口匹配
```json
{
  "localaddr": ":1086",
  "remoteaddr": "[2001:19f0:xxxx:xxxx:xxxx:xxxx:xxxx]:29900",
  "key": "xbw12138",
  "crypt": "aes",
  "mode": "fast3",
  "mtu": 1350,
  "sndwnd": 512,
  "rcvwnd": 512,
  "datashard": 10,
  "parityshard": 3,
  "dscp": 0,
  "nocomp": false,
  "quiet": false
}
```
#### ss.json

```json
{
    "server":"127.0.0.1",
    "local_address": "127.0.0.1",
    "local_port":1080,
    "server_port":1086,
    "password":"xbw12138",
    "timeout":300,
    "method":"aes-256-cfb"
}
```
#### ipv6.py
校园网登录脚本，例如
登录 python ipv6.py login S20186184X 123456
注销 python ipv6.py logout

#### ipv6.sh
整合一键启动
./ipv6.sh
输入网关账号密码直接进行网络连接

#### kcptun
kcptun客户端
./kcptun -c config/kcptun.json

#### log
日志

### proxychains使用方法

配置文件在src/proxychains.conf中配置
使用方法
./proxychains4 -q -f src/proxychains.conf wget www.baidu.com
可以使用别名代替，例如

vim ~/.bashrc
在文件最后追加
```shell
alias pc='/home/bowen/ipv6/proxychains/proxychains4  -q -f /home/bowen/ipv6/proxychains/src/proxychains.conf'
```
source ~/.bashrc

之后就可以直接使用 pc wget www.baidu.com

## 启动方法
1. 自建脚本
![](https://github.com/xbw12138/bjut_ipv6/blob/master/image.png)
2. 登录
![](https://github.com/xbw12138/bjut_ipv6/blob/master/image2.png)
3. 注销
![](https://github.com/xbw12138/bjut_ipv6/blob/master/image3.png)

