# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 320
}

# Initialize total investment
total_investment = 0
portfolio_summary = []

print("=== Stock Portfolio Tracker ===")

while True:
    stock_name = input("Enter stock name:= ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity:= "))
        price = stock_prices[stock_name]
        investment = quantity * price
        total_investment += investment
        
        portfolio_summary.append(
            f"{stock_name}, Quantity: {quantity}, Price: {price}, Investment: {investment}"
        )
        
        print(f"{stock_name} investment: ${investment}\n")
    else:
        print("Stock not found in our price list.\n")

# Display total investment
print("\n=== Portfolio Summary ===")
for item in portfolio_summary:
    print(item)

print(f"\nTotal Investment Value: ${total_investment}")
