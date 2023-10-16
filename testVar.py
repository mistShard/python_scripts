import pandas as pd
import pandas.io.formats.style
import os
from pandas import ExcelWriter
import numpy as np

from xlsxwriter.utility import xl_rowcol_to_cell

writer = pd.ExcelWriter('test1.xlsx', engine='xlsxwriter', options={'strings_to_numbers': True}, date_format='mmmm dd yyyy')  
#df = pd.read_csv("D:\\Users\\u700216\\Desktop\\Reports\\CD_Counts.csv")
df = pd.read_csv("CD_Counts.csv")
df.to_excel(writer, sheet_name='Sheet1', startrow=1 , startcol=0, header=False, index=False, encoding='utf8')  
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

format_header = workbook.add_format()
format_header.set_align('center')
format_header.set_bold()
format_header.set_text_wrap()
format_header.set_border()

format_data = workbook.add_format()
format_data.set_align('center')
format_data.set_text_wrap()

worksheet.set_column('A:Z', 20, format_data)
worksheet.set_row(0, 40, format_header)

# Write the header manually
for colx, value in enumerate(df.columns.values):
    worksheet.write(0, colx, value)