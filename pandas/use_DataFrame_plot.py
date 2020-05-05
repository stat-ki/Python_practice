import numpy as np
import pandas as pd
import os
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt

# os.chdir(r"PATH")
df = pd.read_csv("sample.csv")

df.plot()
print("Close window to go next")
plt.show()

df.plot.bar(stacked = True)
print("Close window to go next")
plt.show()

df.plot.scatter("Attribution 1", "Attribution 2")
print("Close window to go next")
plt.show()

df["Total"] = df.sum(axis = 1)
df["Total"].plot.hist()
print("Close window to go next")
plt.show()