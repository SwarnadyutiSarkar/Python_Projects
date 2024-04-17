import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

def plot_portfolio_value(portfolio_value):
    plt.figure(figsize=(10, 6))
    for ticker in portfolio_value.columns:
        plt.plot(portfolio_value.index, portfolio_value[ticker], marker='o', linestyle='-', label=ticker)
    plt.title('Portfolio Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value ($)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Define stocks and allocations
    stocks = {
        'AAPL': 0.5,
        'MSFT': 0.3,
        'GOOGL': 0.2
    }

    start_date = '2020-01-01'
    end_date = '2021-01-01'
    initial_investment = 10000

    portfolio_value = {}
    dividends_received = {}

    for ticker, allocation in stocks.items():
        data = fetch_stock_data(ticker, start_date, end_date)
        
        # Calculate number of shares
        initial_price = data['Close'].iloc[0]
        shares = (initial_investment * allocation) / initial_price
        
        # Calculate dividends
        dividends = (data['Dividends'] * shares).fillna(0)
        dividends_received[ticker] = dividends.sum()
        
        # Calculate stock value over time
        value = shares * data['Close']
        portfolio_value[ticker] = value

    # Calculate total portfolio value
    total_value = sum(portfolio_value.values())
    portfolio_value['Total'] = total_value

    # Convert dictionaries to DataFrame
    portfolio_value = pd.DataFrame(portfolio_value)
    dividends_received = pd.Series(dividends_received, name='Dividends')

    # Plot portfolio value
    plot_portfolio_value(portfolio_value)

    # Print dividends received
    print("\nDividends Received:")
    print(dividends_received)

if __name__ == '__main__':
    main()
