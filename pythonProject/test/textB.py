# author:cycsir  time:2021/1/22
'''
beautifulSoup:
-Tag
-NavigableString
'''

import requests
import pprint

url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076032286908003&page=2510'
re = requests.get(url)
pprint.pprint(re)


