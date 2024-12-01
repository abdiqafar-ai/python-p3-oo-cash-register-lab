class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.item_prices = []  # Track the prices of each item

    def add_item(self, name, price, quantity=1):
        for _ in range(quantity):
            self.items.append(name)
            self.item_prices.append(price)  # Track the price for each item
            self.total += price

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)
            # Format the output to not show decimals when the total is a whole number
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        if self.items:  # Check if there are items to void
            last_item_price = self.item_prices.pop()  # Remove the price of the last item
            self.items.pop()  # Remove the last item
            self.total -= last_item_price  # Subtract the price of the last item from the total

            # If there are no more items, set total to 0
            if not self.items:
                self.total = 0.0
        else:
            print("No transactions to void.")
