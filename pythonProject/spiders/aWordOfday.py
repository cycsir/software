# author:cycsir  time:2021/1/20
# word_of_everyday1.py
import re  # 正则
import requests
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import sqlite3  # 数据库


# 读第一页，获取所有每日一词链接，访问链接，获取并输出每日一词和相关词汇及对应链接，当页所有链接访问并输出完毕后，读取下一页


def readpage(page, label, attr):
    # 读取页面中各个每日一词的对应链接，label为指定标签，attr为指定标签中的属性
    wordurlList = []
    # 对每一页都单独创建一格新的每日一词链接列表以供访问
    banwordList = ['Chinadaily', 'com', 'cn']
    r = requests.get(page)
    coding = r.apparent_encoding
    t = r.text
    soup = BeautifulSoup(t, "html.parser")
    for target in soup.find_all(label):
        try:
            value = target.get(attr)
            if len(value) == 72 and value not in wordurlList:  # 不会用re，由于每日一词的链接均为72个字符，以wordurlList记录并排除重复
                wordurlList.append(value)

        except:
            value = ''

    for wordurl in wordurlList:
        r1 = requests.get('https:' + wordurl)
        r1.encoding = r1.apparent_encoding
        t1 = r1.text
        soup1 = BeautifulSoup(t1, "html.parser")
        woed = soup1.find(text=re.compile(r'每日一词'))  # 找第一个有每日一词的语句
        woedList = re.findall('[\u4e00-\u9fa5a-zA-Z]+', woed)  # 在woed中找中英文字符串，组成原始的每日一词

        word = ''
        wordlist = []
        banstrList = [r'.', r'。', r':', r'，', r'∣', r'【知识点】', r'【重要讲话】']  # 排除在页面中有特定字符的字符串
        for i in woedList:
            if i not in banwordList:
                word = word + i + " "
        wordlist.append(word)
        for i in wordlist:
            print(i)

        strtarget = ''
        rlwList = []
        index = 0
        for p in soup1.find_all('p'):  # 将p标签的内容转化为字符串
            strtarget += str(p)
        while index < len(banstrList):  # 在p标签转化的字符串中排除有banstrList中的字符的字符串
            index += 1
            if banstrList[index] in strtarget:
                break
        if index == len(banstrList):
            rlwList.append(strtarget)  # 排除完所有元素后加入
        for relatedword in rlwList:
            if relatedword != '<p> </p>':
                if '<br/>' in relatedword:
                    relatedword = re.sub('<br/>', ' ', relatedword)
                relatedword = relatedword.replace('<p>', '').replace('</p>', '')
            print(relatedword)

        print('https:' + wordurl)


def main():
    recent_page_num = 1
    next_page_num = 2
    last_page_num = 2
    page = "https://language.chinadaily.com.cn/news_hotwords/word_of_the_day/page_1.html"
    label = 'a'
    attr = 'href'
    while recent_page_num <= last_page_num:
        # 从第1页到第13页，翻页
        # urlprocess(url,laber,attr)#在该页完成readpage和getword的全部操作#
        # 对每一页都单独创建一格新的每日一词链接列表以供访问
        readpage(page, label, attr)
        page = page.replace(str(recent_page_num), str(next_page_num))  # 更新为下一页的url，继续处理
        recent_page_num = next_page_num
        next_page_num += 1


main()
