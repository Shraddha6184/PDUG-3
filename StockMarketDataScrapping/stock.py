# import yfinance as yf
# import pandas as pd

# # Define the stock symbols for NSE (note: NSE stocks do not have a suffix in yfinance)
# stock_symbols = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS']  # Add '.NS' suffix for NSE stocks

# # Define the date range
# start_date = '2024-01-01'
# end_date = '2024-06-30'

# # Function to fetch and save data for each stock symbol
# def fetch_stock_data(symbol):
#     try:
#         # Fetch historical data from Yahoo Finance
#         data = yf.download(symbol, start=start_date, end=end_date)
        
#         # Check if data is retrieved successfully
#         if data.empty:
#             print(f"No data found for {symbol} between {start_date} and {end_date}")
#             return
        
#         # Process and save to CSV
#         csv_filename = f"{symbol.split('.')[0]}_NSE.csv"
#         data.to_csv(csv_filename)
#         print(f"Data for {symbol} saved to {csv_filename}.")
        
#     except Exception as e:
#         print(f"Error fetching data for {symbol}: {e}")

# # Loop through each stock and fetch data
# for symbol in stock_symbols:
#     fetch_stock_data(symbol)

# print("Data retrieval complete.")


import yfinance as yf
import pandas as pd

# Define the stock symbols for NSE (note: NSE stocks have '.NS' suffix in yfinance)
stock_symbols = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS']

# Define the date range
start_date = '2024-01-01'
end_date = '2024-06-30'

# Function to fetch and save data for each stock symbol
def fetch_stock_data(symbol):
    try:
        # Fetch historical data from Yahoo Finance
        data = yf.download(symbol, start=start_date, end=end_date)
        
        # Check if data is retrieved successfully
        if data.empty:
            print(f"No data found for {symbol} between {start_date} and {end_date}")
            return
        
        # Reset index to include Date as a column
        data.reset_index(inplace=True)
        
        # Save to CSV
        csv_filename = f"{symbol.split('.')[0]}_NSE.csv"
        data.to_csv(csv_filename, index=False)  # Ensure index=False to avoid extra index column
        print(f"Data for {symbol} saved to {csv_filename}.")
        
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# Loop through each stock and fetch data
for symbol in stock_symbols:
    fetch_stock_data(symbol)

print("Data retrieval complete.")
