# 2. Movie Ticket Pricing

age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").strip().lower()

if age >= 18:
    price = 12
elif age < 18:
    price = 8

if day == "wednesday":
    price = price-2

print("Your ticket price is: ${price}")
