import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pandas as pd

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
#                   np.timedelta64(1, 'h'))
# data = np.cumsum(np.random.randn(len(dates)))
# # ax.plot(dates, data)
# cdf = mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
# ax.xaxis.set_major_formatter(cdf)

df = pd.read_csv('NVDA.csv')
print(df)
prices = df["High"]
x = df["Date"]
ax.plot(x, prices)
plt.show()