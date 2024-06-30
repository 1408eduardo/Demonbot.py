import pandas as pd

# Load historical price data
df = pd.read_csv('price_data.csv', index_col='Date', parse_dates=['Date'])

# Calculate Volume Point of Control (VPoC)
def calculate_vpoc(df):
    # Group data by date and calculate total volume for each day
    daily_volume = df.resample('D')['Volume'].sum()
    
    # Find the date with the highest traded volume
    vpoc = daily_volume.idxmax()
    
    return vpoc

vpoc = calculate_vpoc(df)

print(f'Volume Point of Control (VPoC): {vpoc}')
