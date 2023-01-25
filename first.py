import pandas as pd

df = pd.read_excel(
    r'C:\Users\joel.kuhl\Documents\tutorials\tut-vba-py\marks.xlsx', engine="openpyxl")


fromClassA = df[df['Class'].str.match('A')]
numberIn = df[df['Students'].str.contains('2')]
groupBy = df.groupby('Class')


print(fromClassA, numberIn, groupBy.get_group("A").mean())
