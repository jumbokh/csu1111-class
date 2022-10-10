# ch29_2.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

stock2330 = twstock.Stock("2330")
plt.title("台積電", fontsize=24)
plt.plot(stock2330.price)
plt.show()

