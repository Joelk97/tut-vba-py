import pandas as pd

df = pd.read_excel(
    r'C:\Users\joel.kuhl\Documents\tutorials\tut-vba-py\marks.xlsx', engine="openpyxl")

results = df.columns
print(results)
