# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 330
}

total_investment = 0
portfolio_details = []

print("📈 Stock Portfolio Tracker\n")

num_stocks = int(input("Enter number of different stocks you own: "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock_name}, Quantity: {quantity}, Value: ${investment}"
        )

        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found in price list.")

print("\n💼 Total Investment Value: $", total_investment)

# Optional: Save results to a file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")
    for detail in portfolio_details:
        file.write(detail + "\n")
    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\n📁 Portfolio saved to 'portfolio.txt'")
