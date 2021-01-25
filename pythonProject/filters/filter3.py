# author:cycsir  time:2021/1/24
import xlrd
import xlwt
import re
import os
import Weibo
import filter1
import filter2


def filer3():
    textnames = []
    savepaves = (
        ".\\21人民网\\",
        ".\\22央视新闻\\",
        ".\\23半月谈\\"
    )
    file_dir = filter2.savepaves[2]
    savepave = savepaves[2]

    frm0 = ".*Dec.*|.*Jan [0-1].*|.*Jan 2[0-2]"  # 12.22--1.22
    frm1 = ".*Jan 2[3-9].*|.*Jan 3.*|.*Feb 0[0-7].*"  # 1.23-2.7
    frm2 = ".*Feb 1.*|.*Mar 0.*"  # 2.10--2.13
    frm3 = ".*Mar [1-3].*|.*A.*|.*Jun.*"  # 3.10--6.30


    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件

        for file in files:
            if os.path.splitext(file)[1] == '.xls':
                textnames.append(os.path.splitext(file)[0])

    workbook = xlwt.Workbook(encoding="utf-8")
    newsheet = initSheet(workbook, sheetNum=1)
    rows = 1

    newtext = "newtext.txt"
    for textname in textnames:
        try:
            filter1.filter(file_dir, textname, savepave, frm2, 2)
        except:
            pass
            continue

    for textname in textnames:
        realpath = savepave + textname + ".xls"
        try:
            x1 = xlrd.open_workbook(realpath)
        except:
            continue
        sheets = x1.sheets()
        try:
            f = open(newtext, "w", encoding="utf-8")
        except:
            return 0
        for sheet in sheets:
            for row in range(1, sheet.nrows):
                data = sheet.row_values(row, start_colx=0, end_colx=None)  # 返回由该行中所有单元格的数据组成的列表
                for i in range(0, len(data)):
                    newsheet.write(rows, i, data[i])  # 按行写入数据
                rows += 1
    workbook.save(savepave + "半月谈2020.02.10--2020.03.09.xls")


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


filer3()
