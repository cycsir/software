# author:cycsir  time:2021/1/24
import xlrd
import xlwt
import re
import os
import Weibo
import filter1
textnames = []
savepaves = (
    ".\\11人民网\\",
    ".\\12央视新闻\\",
    ".\\13半月谈\\"
)
file_dir = Weibo.savepave[2]
savepave = savepaves[2]
frm = ""
with open("vocab3.txt", "r", encoding="utf-8") as f:
    for line in f:
        frm += ".*" + line.strip("\n") + ".*|"
frm += ".*疫情.*"
print(frm)

for root, dirs, files in os.walk(file_dir):
    # print(root)  # 当前目录路径
    # print(dirs)  # 当前路径下所有子目录
    # print(files)  # 当前路径下所有非目录子文件

    for file in files:
        if os.path.splitext(file)[1] == '.xls':
            textnames.append(os.path.splitext(file)[0])

for textname in textnames:
    try:
        filter1.filter(file_dir, textname, savepave, frm, 0)
    except:
        pass
        continue
