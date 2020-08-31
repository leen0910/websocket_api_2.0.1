# with open("out.txt", "r",encoding='UTF-8') as f:
#     for line in f.readlines():
#         line = line.strip('\n')  #去掉列表中每一个元素的换行符
#         print(line)

# import pandas as pd
# data = pd.read_csv('out.txt', header=None,index_col=0)
#
# print(data)




import csv

with open('out.csv', 'w+', newline='',encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(["记录时间","打表值"])
    # 读要转换的txt文件，文件每行各词间以字符分隔
    with open('out.txt', 'r', encoding='utf-8') as filein:
        for line in filein:
            line_list = line.strip('\n').split(',')
            writer.writerow(line_list)