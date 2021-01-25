# author:cycsir  time:2021/1/22
import Weibo
import spider
import time
def main():
    url = Weibo.urls[2]
    startpage = Weibo.startpages[2]
    lastpage = Weibo.lastpages[2]
    savepath = Weibo.savepave[2]
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