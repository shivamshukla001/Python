items= []
prices = []
total = 0

while True:
    item = input("Enter the item name (or type 'Q' to finish): ").lower()
    if item == 'q':
        break
    else:
        price = float(input("Enter the price of these item "))
        items.append(item)      
        prices.append(price)
        print(f"{item} has been added to the cart.")

for item in items:
    print(f"{item } added to the cart")

for price in prices:
    total += price

print(f"Your total price is: ${total:.2f}")