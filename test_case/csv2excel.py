import pandas as pd
import openpyxl

def csv_to_xlsx_pd():
    csv = pd.read_csv(r'out.csv', encoding='utf-8')
    csv.to_excel(r'out.xlsx', sheet_name='重复精度测试', encoding='utf_8_sig', index=False)


if __name__ == '__main__':
    csv_to_xlsx_pd()