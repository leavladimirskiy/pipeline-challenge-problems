import csv
import random
from datetime import datetime, timedelta

# Settings
filename = "price_data.csv"
num_rows = 100  # adjust as needed
start_date = datetime(2022, 1, 1)

# Column headers
headers = ["timestamp", "symbol", "price", "volume"]

# Sample stock symbols
symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

def maybe_null(value, null_probability=0.05):
    return value if random.random() > null_probability else None

# Write CSV
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    
    for i in range(num_rows):
        timestamp = (start_date + timedelta(seconds=i * 60)).isoformat()
        symbol = random.choice(symbols)
        price = maybe_null(round(random.uniform(100, 1500), 2))
        volume = maybe_null(random.randint(100, 10000))
        
        writer.writerow([timestamp, symbol, price, volume])

print(f"Generated {filename} with {num_rows} rows.")
