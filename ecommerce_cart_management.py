class Cart():
    def __init__(self,items):
        self.cartItems = items
    def get_total(self):
        total = 0
        no_of_items = len(self.cartItems)

        # Iterating over the items in the cart to calculate the Total Price
        for price in self.cartItems.values():
            total += price
        
        return total*0.9 if no_of_items>5 else total

# Input: cart items
items = {}
n = int(input("Enter no of items: "))
for i in range(n):
    name = input("Enter a cart item: ")
    items[name]=int(input("Enter item's price: "))

cart = Cart(items)
total_price = cart.get_total()

# Output: total price
print("Total Price:",total_price)