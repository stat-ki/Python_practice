import matplotlib

matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)
plt.hist(data, bins = 20)

plt.title("Histgram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()