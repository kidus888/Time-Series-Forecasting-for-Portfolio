
import matplotlib.pyplot as plt

def plot_closing_price(data):
    """Plot closing prices for each asset."""
    plt.figure(figsize=(14, 8))
    for ticker, df in data.items():
        plt.plot(df.index, df['Close'], label=ticker)
    plt.title("Closing Prices of Assets")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.legend()
    plt.show()

def plot_daily_returns(df, ticker):
    """Plot daily returns for a single asset."""
    df['Daily Return'] = df['Adj Close'].pct_change()
    df['Daily Return'].plot(title=f"Daily Returns of {ticker}", figsize=(10, 6))
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.show()
