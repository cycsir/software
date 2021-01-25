import sys
from bs4 import BeautifulSoup
import re
import urllib.request
import json
import gzip
from io import BytesIO
import xlwt
import pprint
import requests
import Weibo
import time



def main(url, startpage, lastpage, savepath, head):
    baseurl = 'https://m.weibo.cn/api/container/getIndex?containerid=' + url + '&page={}'
    page = getData(baseurl, startpage, lastpage, savepath, head)  # 1.爬取网页
    return page

# 2.逐一解析数据（一边爬取一边解析）
# 3.保存数据



def getData(url, startpage, lastpage, savepath, head):
    # create a workboot
    pageNum = 0  # 页数，记录已经爬取的微博页数
    row = 0
    sheetNum = 0
    workbook = ""
    sheet = ""
    page = lastpage
    for i in range(lastpage, startpage):
        if pageNum == 0:
            workbook = xlwt.Workbook(encoding="utf-8")
            sheet = initSheet(workbook, sheetNum)
            sheetNum += 1
            row = 1
        try:
            re = requests.post(url.format(page), headers=head)
            # 转变为json格式
            datas = re.json()
            # pprint.pprint(datas)
            cards = datas['data']['cards']
            for card in cards:
                sheet = saveData(card, sheet, row, head)
                row += 1
        except KeyError:
            print(KeyError)
            workbook.save(savepath + "book%d.xls" % i)
            return page
        # cards = datas['data']['cards']
        except requests.exceptions.SSLError:
            print(requests.exceptions.SSLError)
            workbook.save(savepath + "book%d.xls" % i)
            return page
        except:
            print("Other error")
            workbook.save(savepath + "book%d.xls" % i)
            return page
        # except:
        #     if cookies == 0:
        #         cookies = 1
        #     else:
        #         cookies = 0
        #     header = headers[cookies]
        #     continue
        # except:
        #     pass
        #     print("page%d failed"%page)
        #     continue
        # cards 一条微博
        print("recent Page is %d" % i)
        pageNum += 1
        if pageNum >= 20:
            workbook.save(savepath + "book%d.xls" % i)
            print("recent book is %d" % i)
            pageNum = 0
            time.sleep(20)
        page += 1
    workbook.save(savepath + "book%d.xls" % startpage)

def saveData(card, sheet1, row, head):
    global data
    pat = re.compile("<span.*?span>|<a.*?a>")
    if card.get('mblog', None):
        text = re.sub(pattern=pat, repl="", string=card['mblog']['text'])  # 微博正文
        scheme = card['scheme']  # 微博地址
        created_at = card['mblog']['created_at']  # 时间
        comments_count = card['mblog']['comments_count']  # 评论数
        attitudes_count = card['mblog']['attitudes_count']  # 点赞数
        reposts_count = card['mblog']['reposts_count']  # 转发数
        weibo = (
            text,
            scheme,
            created_at,
            comments_count,
            attitudes_count,
            reposts_count
        )
        for col in range(0, 6):
            sheet1.write(row, col, weibo[col])
        col = 6

        mid = card['mblog']['mid']
        response = requests.post(
            url='https://m.weibo.cn/comments/hotflow?id={mid}&mid={mid}&max_id_type=0'.format(mid=mid),
            headers=head
        )
        data = response.json()
        users = data.get('data', None)
        if users:
            users = users['data']
            for user in users:
                comment_texts = user['text']
                comment_texts = re.sub(pattern=pat, repl="", string=comment_texts)
                sheet1.write(row, col, comment_texts)
                col += 1
    return sheet1


def initSheet(workbook, sheetNum):
    sheet1 = workbook.add_sheet("sheet%d" % sheetNum)
    sheet1.write(0, 0, "微博正文")
    sheet1.write(0, 1, "微博地址")
    sheet1.write(0, 2, "时间")
    sheet1.write(0, 3, "评论数")
    sheet1.write(0, 4, "点赞数")
    sheet1.write(0, 5, "转发数")
    sheet1.write(0, 6, "评论")
    return sheet1


if __name__ == "__main__":
    main()

    ## 定义主函数位置 管理程序内函数关系
