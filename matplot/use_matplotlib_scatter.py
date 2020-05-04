import matplotlib

matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import numpy as np

datax = np.random.randn(100)
datay = datax + np.random.randn(100)*0.3

plt.scatter(datax, datay, label = "Data 1")

datax = np.random.randn(100)
datay = 0.6*datax + np.random.randn(100)*0.4

plt.scatter(datax, datay, color = "red", label = "Data 2")


plt.title("Sample")
plt.xlabel("Vertical axis")
plt.ylabel("Horizontal axis")
plt.legend()
plt.show()