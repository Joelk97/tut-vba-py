import xlwings as xw
import pandas as pd


wk = xw.books.open(r'C:\Users\joel.kuhl\Documents\tutorials\tut-vba-py\marks.xlsx')
sheet = wk.sheets("Results")
rg = sheet.range("A1:C2")

df = sheet.range("B1:D13").options(pd.DataFrame).value
df = df[:2]
'''print(rg.value)'''

print(df)
xw.view(df) # opens new Excel with data frame in it

wk.close