import numpy as np
import pandas as pd
import os

# os.chdir(r"PATH")
df = pd.read_csv("sample.csv")

df["Total"] = df.sum(axis = 1)
print(df)
print(df.describe())