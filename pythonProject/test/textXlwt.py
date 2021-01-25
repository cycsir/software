# author:cycsir  time:2021/1/22

import xlwt

# workbook = xlwt.Workbook(encoding="utf-8")  # create a workboot
# worksheet = workbook.add_sheet('sheet1')
#
# worksheet.write(0, 0, 'hello')
# workbook.save('student.xls')

workbook = xlwt.Workbook(encoding="utf-8")  # create a workboot
worksheet = workbook.add_sheet('sheet1')
worksheet.add(0,0,"1")
workbook.save('student.xls')

header1 = {
        "cookie": "SUB=_2A25NA5ziDeThGeNN61IZ9i_EwzqIHXVuDySqrDV6PUJbktAKLU74kW1NScdmAZozUPCe0F7eylt2zMy9qhd-OTFE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWozF7q_JZ7Mvh.HDJerxx-5NHD95Qfe0571hqp1hncWs4Dqcjni--fi-2XiKLWi--fi-2XiKLWi--ci-zXiKLFS0nESKBt; SSOLoginState=1611132083; _T_WM=78352212005; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032286908003%26fid%3D1076032286908003%26uicode%3D10000011; XSRF-TOKEN=b2e19b",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }  # page

header2 = {
        "cookie": "WEIBOCN_FROM=1110006030; SUB=_2A25ND3unDeRhGeBO41sT-SvOyjiIHXVu8AXvrDV6PUJbkdAKLUbzkW1NRYkdIYl0zA8ZuOvtGKtD858aKoOHMNpa; _T_WM=96389282857; MLOGIN=1; XSRF-TOKEN=44d1ff; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076031699432410%26oid%3D4445537375865878%26uicode%3D20000061%26fid%3D4445537375865878",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    }  # page

header3 = {
":authority": "m.weibo.cn",
":method": "GET",
":path": "/api/container/getIndex?uid=2286908003&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%BA%BA%E6%B0%91%E7%BD%91&type=uid&value=2286908003&containerid=1005052286908003",
":scheme": "https",
"accept": "application/json, text/plain, */*",
"accept-language": "zh-CN,zh;q=0.9",
"cookie": "_T_WM=96389282857; WEIBOCN_FROM=1110006030; XSRF-TOKEN=526321; loginScene=102003; SUB=_2A25ND70cDeRhGeFL7lYZ8ynKyTyIHXVu88NUrDV6PUJbktANLVHakW1NfeCpB2THRSjIiXmMEwOZemcERCIBgH1S; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFVzXU6ciuTrqpsinSDlxAg5JpX5KzhUgL.FoMfSKBRe0Mceo52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNSK-X1heNSoz7; SSOLoginState=1611386188; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E4%25BA%25BA%25E6%25B0%2591%25E7%25BD%2591%26fid%3D1005052286908003%26uicode%3D10000011mweibo-pwa: 1",
"referer": "https://m.weibo.cn/u/2286908003?uid=2286908003&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%BA%BA%E6%B0%91%E7%BD%91",
 #"sec-ch-ua": "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
"sec-ch-ua-mobile": "?0",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
"x-requested-with": "XMLHttpRequest",
"x-xsrf-token": "526321",
}










