# 📈 Stock Ticker Terminal Display

This Python script provides a real-time scrolling display of stock prices and their percentage changes directly in your terminal. 

## Features

- 🔄 Real-time updates: Stock prices are updated in real time during market hours.
- 🎨 Color-coded changes: Price increases are displayed in green, and decreases are displayed in red.
- 🔄 Continuous scrolling: Stock information continuously scrolls across the terminal.
- 🛠 Configurable: Easily add or remove stocks from the display via a configuration file.

## Installation

1. **Clone the repository**:  
   ```sh
   git clone https://github.com/yourusername/stock-ticker-terminal
   cd stock-ticker-terminal

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
3. Run the script:
   ```sh
  python scrollticker.py

## Configuration

To configure the stocks that appear in the ticker, edit the tickers.txt file. Add each stock ticker symbol that you want to display on a new line.


## Dependencies

Python 3.6+: The software is written in Python, and requires a version of Python that is 3.6 or newer.<br>
yfinance: This package is used to fetch stock data from Yahoo Finance.<br>
pytz: This package is used for timezone calculations, helping to determine when the stock market is open.<br>

To install all required dependencies, run: 
```sh
pip install -r requirements.txt
