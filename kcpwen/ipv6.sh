#!/bin/sh
work_path=$(dirname $(readlink -f $0))
cd ${work_path}
read -p "输入网关账号:" username
if [ ! -n "$username" ]
then
    echo "请输入网关账号"
    exit;
else
    read -p "输入网关密码:" password
    if [ ! -n "$password" ]
    then
        echo "请输入网关密码"
        exit;
    else
        msg=$(python ipv6.py login ${username} ${password})
        if [ "$msg" = "ipv6登录成功" ]
        then
            echo 'ipv6登录成功'
        else
            echo 'ipv6登录失败'
            exit;
        fi
    fi
fi
nohup ./kcptun -c config/kcptun.json >log/kcptun 2>&1 &
nohup sslocal -c config/ss.json >log/ss 2>&1 &

content=$(../proxychains/proxychains4 -q -f ../proxychains/src/proxychains.conf curl -I -m 10 -o /dev/null -s -w %{http_code} www.baidu.com)
if [ $content != 200 ]
then
    echo '网络连接失败，请查看log日志'
else
    echo '网络连接成功\n使用proxychains全局代理\n例如\n../proxychains/proxychains4 -q -f ../proxychains/src/proxychains.conf wget www.baidu.com\n或者使用别名 pc wget www.baidu.com';
    exit;
fi