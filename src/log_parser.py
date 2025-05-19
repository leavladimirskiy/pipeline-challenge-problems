import pandas as pd

file_path = "/Users/leastavnitser/Projects/price_data.csv"

def parse_log_file(file_path):
    
    # Read the CSV df
    df = pd.read_csv(file_path)

    null_count = df.isnull().sum().sum()
    return null_count, df


nulls, data = parse_log_file(file_path)
print(f"Null values: {nulls}")