import pandas as pd
import time
from datetime import datetime 
from collections import deque


df = pd.read_csv("cleaned_data.csv", parse_dates=["timestamp"])
df['price'] = pd.to_numeric(df['price'], errors='coerce')


window = deque(maxlen=30)

for i, row in df.iterrows():
        price = row["price"]
        window.append(price)

        avg = sum(window) / len(window) 
        print({
                'timestamp': row['timestamp'],
                'symbol': row['symbol'],
                'price': price,
                'average_price': round(avg, 2)
            })        
        
        time.sleep(.10) 