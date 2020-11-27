#coding=utf-8
import xlwt


 # 为样式创建字体
font = xlwt.Font()

# # 字体类型
# font.name = 'name Times New Roman'
# # 字体颜色
# font.colour_index = i
# # 字体大小，11为字号，20为衡量单位
# font.height = 20*11
# 字体加粗
font.bold = True
# # 下划线
# font.underline = True
# # 斜体字
# font.italic = True

# 设置单元格对齐方式
alignment_center = xlwt.Alignment()
# 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
alignment_center.horz = 0x02
# 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
alignment_center.vert = 0x01

# # 设置自动换行
# alignment.wrap = 1

# 设置单元格对齐方式
alignment_left = xlwt.Alignment()
# 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
alignment_left.horz = 0x01
# 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
alignment_left.vert = 0x00


# 初始化样式
style0 = xlwt.XFStyle()
style0.font = font

style2 = xlwt.XFStyle()
style2.alignment = alignment_center

style3 = xlwt.XFStyle()
style3.alignment = alignment_left

style = "font:colour_index red;"
red_style = xlwt.easyxf(style)





workbook = xlwt.Workbook()
sheet1=workbook.add_sheet('重复精度测试',cell_overwrite_ok=True)
#style = "font:colour_index blue;"
#blue_style = xlwt.easyxf(style)

row0=[u"重复次数",u"打表时间",u"打表值",u"偏差值(mm)",u"测试结果"]
for i in range(0,len(row0)):
    sheet1.write(0,i,row0[i],style0)
    #sheet1.write(0,i,row0[i],blue_style)


f = open('out.txt', encoding = 'utf-8',errors='ignore')
# next(f)
zeo=f.readline().strip('\n').split(',')[1]
index = 1
i=1
count_p=0
count_f=0
jingdu=0.03

for line in f:
    data = line.strip('\n').split(',')


    # print (data)
    piancha=(float(data[1])-float(zeo))/100
    sheet1.write(index,0,i,style2)
    sheet1.write(index,1,data[0],style2)
    sheet1.write(index,2,float(data[1]),style2)
    sheet1.write(index,3,piancha,style2)
    if piancha <= jingdu and piancha >= -jingdu:
        sheet1.write(index,4,"pass",style2)
        count_p=count_p+1
    else:
        sheet1.write(index,4,"failed",red_style)
        count_f=count_f+1

    index = index + 1
    i=i+1


sheet1.write(index,0,"标准精度偏差：",style0)
sheet1.write(index,1,"± %s"%jingdu,style3)
sheet1.write(index+1,0,"合格次数：",style0)
sheet1.write(index+1,1,count_p,style3)
sheet1.write(index+2,0,"失败次数：",style0)
sheet1.write(index+2,1,count_f,style3)
sheet1.write(index+3,0,"总测试次数：",style0)
sheet1.write(index+3,1,i-1,style3)
sheet1.write(index+4,0,"不良率：",style0)
sheet1.write(index+4,1,'{:.2f}%'.format(count_f/(i-1)*100),style3)


sheet1.col(0).width = 4444
sheet1.col(1).width = 5555
sheet1.col(2).width = 2222
sheet1.col(3).width = 3333
sheet1.col(4).width = 2222
workbook.save('out1.xls')