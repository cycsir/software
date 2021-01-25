# author:cycsir  time:2021/1/24
# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
import xlwt
import xlrd
import Weibo
import os

basepath = Weibo.savepave[1]

'''
遍历某个目录下的所有xls文件，并将文件中的第一列--微博正文按行转存至txt文件
@pram file_dir: 目录路径
        num: 要遍历的文件数量

'''


def file_name(file_dir):
    global len
    L = []
    num = int(len(L) / 4)
    keyworks = []
    filename = "file1.txt"
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件

        for file in files:
            if os.path.splitext(file)[1] == '.xls':
                L.append(os.path.join(root, file))
    # print(len(L))

    with open(filename, "w", encoding="utf-8") as file1:
        for i in range(61, 120):
            file = AxlsTotxt(L[i])
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    file1.write(line)
            f.close()
    with open("file1.txt", "r", encoding="utf-8") as file1:
        for line in file1:
            print(line)
    return filename


'''
对一个xls的某些内容进行操作进行操作，返回一个TXT文件名
'''


def AxlsTotxt(filename):
    realpath = filename
    print(realpath)
    newtext = "newtext.txt"
    try:
        x1 = xlrd.open_workbook(realpath)
    except:
        return newtext
    sheets = x1.sheets()
    f = open(newtext, "w", encoding="utf-8")
    for sheet in sheets:
        cownum = sheet.ncols
        for cow in range(6, cownum):
            for text in sheet.col_values(cow, 0, 250):
                f.write(text + "\n")
    f.close()
    return newtext


def BxlsTotxt(filename):
    realpath = filename
    print(realpath)
    newtext = "newtext.txt"
    try:
        x1 = xlrd.open_workbook(realpath)
    except:
        return newtext
    sheets = x1.sheets()
    f = open(newtext, "w", encoding="utf-8")
    for sheet in sheets:
        for text in sheet.col_values(0, 0, 250):
            f.write(text + "\n")
    f.close()
    return newtext


'''
分词操作
'''


def txttoword(filename):
    text = ""
    words = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            text += line

            # 分词
            for word in jieba.cut(line):
                words.append(word)

    # 词表去重
    words = list(set(words))
    with open('vocab1.txt', 'w', encoding="utf-8") as vf:
        for w in words:
            vf.write(w + "\n")

    with open('vocab2.txt', 'w', encoding="utf-8") as vf:
        for word in jieba.analyse.textrank(sentence=text, topK=4000, withWeight=False):
            vf.write(word+'\n')

    with open('vocab2.txt', 'r', encoding="utf-8") as vf:
        for line in vf:
            print(line)


filename = file_name(file_dir=basepath)
txttoword(filename)

