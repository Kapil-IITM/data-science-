import pandas as pd

df = pd.read_csv("Used_Bikes.csv",encoding="latin1")

# print(df.to_string())

# var = df.head(10)
# var1 = df.tail(10)
var3 = df.info()
# print(var)
# print(var1)
print(var3)
print(df.describe())
print(df.dtypes)