import matplotlib

matplotlib.use("tkagg")
import matplotlib.pyplot as plt

# matplotlib.rc("font", **{"family": "Yu Gothic"})

plt.plot([1, 2, 3], "k-", label = "Series 1")
plt.plot([2, 3, 4], "r--", label = "Series 2")
plt.plot([3, 4, 5], "b--o", label = "Series 3")

plt.title("Sample")
plt.xlabel("Vertical axis")
plt.ylabel("Horizontal axis")
plt.legend()
plt.show()