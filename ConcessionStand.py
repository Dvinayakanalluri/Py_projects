
menu = {
    "pizza": 10.99,
    "hot dog": 5.99,
    "soda": 1.99,
    "popcorn": 4.99,
    "candy": 2.99,
    "nachos": 6.99,
    "pretzel": 3.99,
    "water": 1.49,
    "coffee": 2.49,
    "tea": 1.99,
    "ice cream": 3.49
}

cart = []
total = 0.0

print("-----------MENU-----------")
for item, price in menu.items():
    print(f"{item.title()}: ${price:.2f}")
print("--------------------------")

while True:
    item = input("Enter an item to add to your cart (or 'done' to finish): ").lower()
    if item == "done":
        break
    if item in menu:
        cart.append(item)
        total += menu[item]
    else:
        print("Item not found in the menu.")

print(f"\nTotal: ${total:.2f}")
print("Items in cart:")
for item in cart:
    print(f"- {item.title()}")

    