import urllib.request

import pandas as pd

column = ["ticker"]

df = pd.read_csv("alltickers.csv", names=column)

tickers = df.ticker.to_list()

size = len(tickers)

i = 0

while i < size:
    ticker = tickers[i]
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + ticker + "?period1=1167609600&period2=1616889600&interval=1d&events=history&includeAdjustedClose=true"
    urllib.request.urlretrieve(url, "C:\\Documents\\" + ticker + ".csv")
    time.sleep(0.5)
    i += 1