import json
import os

STOCK_PRICES = {
    "AAPL": 195,
    "GOOGL": 180,
    "MSFT": 450,
    "TSLA": 260,
    "AMZN": 200,
    "NVDA": 130,
    "META": 510
}

FILE_NAME = "portfolio.json"


class Portfolio:
    def __init__(self):
        self.stocks = {}
        self.load()

    def buy(self):
        stock = input("Enter Stock Symbol: ").upper()

        if stock not in STOCK_PRICES:
            print("Stock not available.")
            return

        qty = int(input("Enter Quantity: "))

        if stock in self.stocks:
            self.stocks[stock] += qty
        else:
            self.stocks[stock] = qty

        print("Stock purchased successfully!")

    def sell(self):
        stock = input("Enter Stock Symbol: ").upper()

        if stock not in self.stocks:
            print("Stock not found.")
            return

        qty = int(input("Enter Quantity: "))

        if qty > self.stocks[stock]:
            print("Not enough shares.")
            return

        self.stocks[stock] -= qty

        if self.stocks[stock] == 0:
            del self.stocks[stock]

        print("Stock sold successfully!")

    def view(self):
        if not self.stocks:
            print("Portfolio Empty")
            return

        total = 0

        print("\n------ Portfolio ------")
        print("{:<10}{:<10}{:<10}".format("Stock", "Qty", "Value"))

        for stock, qty in self.stocks.items():
            value = qty * STOCK_PRICES[stock]
            total += value
            print("{:<10}{:<10}{:<10}".format(stock, qty, value))

        print("-----------------------")
        print("Total Value: $", total)

    def search(self):
        stock = input("Enter Stock Symbol: ").upper()

        if stock in STOCK_PRICES:
            print(stock, "Current Price = $", STOCK_PRICES[stock])
        else:
            print("Stock not available.")

    def save(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.stocks, file)

    def load(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.stocks = json.load(file)


def main():
    portfolio = Portfolio()

    while True:
        print("\n========== SMART STOCK PORTFOLIO ==========")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Search Stock")
        print("5. Save Portfolio")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            portfolio.buy()

        elif choice == "2":
            portfolio.sell()

        elif choice == "3":
            portfolio.view()

        elif choice == "4":
            portfolio.search()

        elif choice == "5":
            portfolio.save()
            print("Portfolio Saved!")

        elif choice == "6":
            portfolio.save()
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()