import matplotlib.pyplot as plt
import xlrd
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)


data = xlrd.open_workbook(r'out1.xls')
table = data.sheets()[0]

x_data=table.col_values(0)
y_data=table.col_values(3)

plt.plot(x_data[1:-6], y_data[1:-6], 'bo', linewidth =1,label='offset')
plt.title('重复精度',fontproperties=font_set)
plt.grid()
plt.legend()

plt.xlabel('重复次数',fontproperties=font_set)
plt.ylabel('偏差量(mm)',fontproperties=font_set)
plt.show()