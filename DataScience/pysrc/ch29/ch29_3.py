# ch29_3.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

stock2330 = twstock.Stock("2330")
stock2330.fetch_from(2022,1)
plt.title("台積電", fontsize=24)
plt.xlabel("2022年1月以來的交易天數", fontsize=14)
plt.ylabel("價格", fontsize=14)
plt.plot(stock2330.price)
plt.show()

