import matplotlib

matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import numpy as np

# Set locations
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.subplots_adjust(hspace = 0.5, wspace = 0.5)

# Line graph
data = np.random.randn(100).cumsum()
ax1.plot(data)

ax1.set_title("Line graph")
ax1.set_xlabel("Time")
ax1.set_ylabel("Location")

# Scatter
datax = np.random.randn(100)
datay = datax + np.random.randn(100)*0.3
ax2.scatter(datax, datay, label = "Data 1")

datax = np.random.randn(100)
datay = 0.6*datax + np.random.randn(100)*0.4
ax2.scatter(datax, datay, color = "red", label = "Data 2")

ax2.set_title("Scatter")
ax2.set_xlabel("Attribution 1")
ax2.set_ylabel("Attribution 2")
ax2.legend()

# Histgram
data = np.random.randn(1000)
ax3.hist(data, bins = 20)

ax3.set_title("Histgram")
ax3.set_xlabel("Values")
ax3.set_ylabel("Frequency")

plt.show()