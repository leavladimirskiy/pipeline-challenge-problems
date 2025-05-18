portfolio = {'AAPL': 30, 'GOOG': 5}
prices = {'AAPL': 170.5, 'GOOG': 2800.75}

def calculate_portfolio_value(portfolio, prices):
    total_value = 0.0
    for symbol, quantity in portfolio.items():
        if symbol in prices:
            total_value += quantity * prices[symbol]
    return total_value
# Example usage

print(calculate_portfolio_value(portfolio, prices))