
import yfinance as yf

def fetch_data(tickers, start_date, end_date):
    """Fetch historical data for given tickers."""
    data = {ticker: yf.download(ticker, start=start_date, end=end_date) for ticker in tickers}
    return data
