import pandas as pd

df1 = pd.read_excel("2021-22 Graduates.xlsx")
df2 = pd.read_excel("2022 Graduation Indicators.xlsx")

df1 = df1.dropna(subset=[df1.columns[0]])
df2 = df2.dropna(subset=[df2.columns[0]])

df1.to_csv("graduates_clean.csv", index=False)
df2.to_csv("indicators_clean.csv", index=False)

print("Done! Files saved.")
