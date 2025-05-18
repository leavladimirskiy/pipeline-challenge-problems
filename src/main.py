import pandas as pd
import numpy as np

filename = "/Users/leastavnitser/Projects/price_data.csv"
df = pd.read_csv(filename)


print(df.head())

df_new = df.dropna()

print(df_new)
df_new.to_csv("cleaned_data.csv", index=True)
