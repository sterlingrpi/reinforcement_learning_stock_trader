import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def get_prices(symbols, start, end):
    prices = []
    for symbol in symbols:
        tickerData = yf.Ticker(symbol)
        tickerDf = tickerData.history(period='1d', start=start, end=end)
        #tickerDf = tickerData.history(period='max')
        prices.append(np.array(tickerDf)[:, 0])
    return prices


if __name__ == '__main__':
    symbols = ['MSFT', 'TSLA', 'AAPL', 'OTRK', 'REGN', 'GTLS', 'CYRX', 'GM']
    start = '2016-1-15'
    end = '2021-9-5'
    prices = get_prices(symbols, start, end)

    for i, price in enumerate(prices):
        print(np.shape(price))
        plt.subplot(2, 4, i + 1)
        plt.plot(price)
        plt.title(symbols[i])
    plt.show()
