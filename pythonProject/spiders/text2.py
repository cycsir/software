# author:cycsir  time:2021/1/22
import Weibo
import spider
import time
def main():
    url = Weibo.urls[1]
    startpage = Weibo.startpages[1]
    lastpage = Weibo.lastpages[1]
    savepath = Weibo.savepave[1]
    header = Weibo.headers[4]
    stops = 0
    while 1:
        lastpage = spider.main(url, startpage, lastpage, savepath, header)
        stops += 1
        print(stops)
        header = Weibo.headers[stops % 5]
        time.sleep(20)
        if stops % 10 == 9:
            print("stopping 2 min")
            time.sleep(120)

main()

# https://pypi.tuna.tsinghua.edu.cn/simple jieba