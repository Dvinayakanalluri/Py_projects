
Food = []
Prices = []
Total = 0

while True:
    item = input("Enter the name of the food item (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    price = float(input(f"Enter the price for {item}: "))
    
    Food.append(item)
    Prices.append(price)
    Total += price

print("\n--- Shopping Cart ---")
for i in range(len(Food)):
    print(f"{Food[i]}: ${Prices[i]:.2f}")

print(f"\nTotal: ${Total:.2f}")