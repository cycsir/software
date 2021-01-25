# author:cycsir  time:2021/1/22
import Weibo
import spider
def main():
    url = Weibo.urls[0]
    startpage = Weibo.startpages[0]
    lastpage = Weibo.lastpages[0]
    savepath = Weibo.savepave[0]
    spider.main(url, 10, 0, savepath)

main()