# author:cycsir  time:2021/1/24

# 对微博进行筛选
import xlrd
import xlwt
import re

def filter(file_dir, textname, savepave, frm, maincol):
    realpath = file_dir + textname + ".xls"
    savepave = savepave + textname + ".xls"
    newtext = "newtext.txt"

    x1 = xlrd.open_workbook(realpath)
    sheets = x1.sheets()
    workbook = xlwt.Workbook(encoding="utf-8")
    newsheet = initSheet(workbook, 1)
    rows = 1
    try:
        f = open(newtext, "w", encoding="utf-8")
    except:
        return 0
    for sheet in sheets:
        for row in range(0, sheet.nrows):
            text = sheet.cell_value(row, maincol)
            if re.match(frm, text):
                data = sheet.row_values(row, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
                for i in range(0, len(data)):
                    newsheet.write(rows, i, data[i])  # 按行写入数据
                rows += 1
    workbook.save(savepave)
    #             rows.append(row)
    #
    #         f.write(text + "\n")
    # f.close()




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
