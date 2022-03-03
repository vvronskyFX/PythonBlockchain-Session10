import pandas as pd
import matplotlib.pyplot as plt

url = 'https://query1.finance.yahoo.com/v7/finance/download/DOGE-USD?period1=1590146414&period2=1621682414&interval=1d&events=history&includeAdjustedClose=true'

df_doge = pd.read_csv(url)
df_doge = df_doge.dropna(axis=0,subset=['Open']) # check
df_doge['Rolling30Vol'] = df_doge['Open'].rolling(30).std()
df_doge['Rolling30Vol'].plot()
plt.show()