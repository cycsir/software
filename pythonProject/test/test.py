# author:cycsir  time:2021/1/20

import requests
import time
import pprint

# get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  # 获得源码并进行utf-8的解码

# post请求 模拟用户登录
# import urllib.parse # 解析器
# data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data= data)
# print(response.read().decoder(“utf-8”))

# 超时解决方案
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decoder("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

# response用途
# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))

# 伪装 封装request
# url = "https://www.douban.com"
# # url = "http://httpbin.org/get"
# # data = bytes(urllib.parser.urlencoder({'name':'eric'}), encoding="utf-8")
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
#
# }
# req = urllib.request.Request(url=url,headers=header)
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076032286908003&page={}'
header = {
"cookie": "SUB=_2A25NA5ziDeThGeNN61IZ9i_EwzqIHXVuDySqrDV6PUJbktAKLU74kW1NScdmAZozUPCe0F7eylt2zMy9qhd-OTFE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWozF7q_JZ7Mvh.HDJerxx-5NHD95Qfe0571hqp1hncWs4Dqcjni--fi-2XiKLWi--fi-2XiKLWi--ci-zXiKLFS0nESKBt; SSOLoginState=1611132083; _T_WM=78352212005; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032286908003%26fid%3D1076032286908003%26uicode%3D10000011; XSRF-TOKEN=b2e19b",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}# page

for i in range(199, 205):
    print(i)
    re = requests.post(url=url.format(i),headers=header)
    # 转变为json格式
    datas = re.json()
    # pprint.pprint(data)
    cards = datas['data']['cards']
    # cards 一条微博
    for card in cards:
        if card.get('mblog', None):
            text = card['mblog']['text']  # 微博正文
            scheme = card['scheme']  # 微博地址
            created_at = card['mblog']['created_at']  # 时间
            comments_count = card['mblog']['comments_count']  # 评论数
            attitudes_count = card['mblog']['attitudes_count']  # 点赞数
            reposts_count = card['mblog']['reposts_count']  # 转发数

            mid = card['mblog']['mid']
            response = requests.get(
                'https://m.weibo.cn/comments/hotflow?id={mid}&mid={mid}&max_id_type=0'.format(mid=mid))
            data = response.json()
            users = data.get('data', None)
            if users:
                users = users['data']
                for user in users:
                    comment_texts = user['text']
                    print(comment_texts)


