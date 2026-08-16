#Compound Interest Calculator

principal = 0
rate = 0
time = 0

while True:
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in %): ")) 
        time = float(input("Enter the time period (in years): "))
        break
    except ValueError:
        print("Invalid input. Please enter numeric values for principal, rate, and time.")

total_amount = principal * (1 + rate / 100) ** time
interest_earned = total_amount - principal
print(f"Total amount after {time} years: ${total_amount:.2f}")
print(f"Interest earned: ${interest_earned:.2f}")