from openpyxl import load_workbook
 
#加载excel，注意路径要与脚本一致
wb = load_workbook('lpl.xlsx')
 
#激活excel表
sheet = wb.active
 
#向excel中写入表头
sheet['a1'] = '上'
sheet['b1'] = '中'
sheet['c1'] = '野'
sheet['d1'] = 'adc'
sheet['e1'] = '辅助'

with open('das.txt',mode='r',encoding='utf-8')as f:
    for i in f:
        i.split(sep=' ')
        for j in i:
            sheet.append(j)
 


 
wb.save('lpl.xlsx')
 
# print('数据写入成功！')