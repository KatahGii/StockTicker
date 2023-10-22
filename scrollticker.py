import yfinance as yf
import time
import os
import sys
from datetime import datetime, time as dt_time, timezone, timedelta
import pytz

def load_tickers(filename="tickers.txt"):
    try:
        with open(filename, 'r') as f:
            tickers = [line.strip() for line in f if line.strip()]
        return tickers
    except FileNotFoundError:
        print(f"Ticker file {filename} not found. Please create it with one ticker symbol per line.")
        sys.exit(1)

def is_market_open():
    eastern = pytz.timezone('US/Eastern')
    now = datetime.now(eastern)
    open_time = dt_time(9, 30)
    close_time = dt_time(16)
    # Check if today is a weekday (0-4 correspond to Monday-Friday)
    if now.weekday() < 5:
        return open_time <= now.time() <= close_time
    return False

def get_stock_data(tickers):
    data = yf.Tickers(' '.join(tickers))
    stock_data = {}
    market_open = is_market_open()
    for ticker in tickers:
        try:
            info = data.tickers[ticker].info
            if market_open and 'regularMarketPrice' in info:
                price = info['regularMarketPrice']
                change = info.get('regularMarketChange', "N/A")
                change_percent = info.get('regularMarketChangePercent', "N/A")
            else:
                price = info.get('previousClose', "N/A")
                change = info.get('postMarketChange', info.get('regularMarketChange', "N/A"))
                change_percent = info.get('postMarketChangePercent', info.get('regularMarketChangePercent', "N/A"))
            stock_data[ticker] = (price, change, change_percent)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {str(e)}")
            stock_data[ticker] = ("N/A", "N/A", "N/A")
    return stock_data

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def scroll_stock_data(stock_data, sleep_duration=0.2):
    terminal_width, _ = os.get_terminal_size()
    ticker_strings = []
    for ticker, (price, change, change_percent) in stock_data.items():
        if isinstance(price, (float, int)) and isinstance(change, (float, int)) and isinstance(change_percent, (float, int)):
            color = '\033[92m' if change_percent >= 0 else '\033[91m'
            reset_color = '\033[0m'
            ticker_string = f"{ticker}: ${price:.2f} {color}{'Δ' if change_percent >= 0 else '▼'}{change:+.2f} ({change_percent:+.2f}%){reset_color}"
        else:
            ticker_string = f"{ticker}: {price} Δ{change} ({change_percent})"
        ticker_strings.append(ticker_string)

    ticker_string = '   '.join(ticker_strings)
    extended_ticker_string = ticker_string + ' ' * terminal_width
    
    position = 0
    try:
        while True:
            print(extended_ticker_string[position:position + terminal_width], end='\r', flush=True)
            position = (position + 1) % len(extended_ticker_string)
            time.sleep(sleep_duration)
    except KeyboardInterrupt:
        clear_terminal()
        print("Exited by user")

def main():
    clear_terminal()
    tickers = load_tickers()
    try:
        stock_data = get_stock_data(tickers)
        scroll_stock_data(stock_data)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
