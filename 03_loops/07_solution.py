# 7. Validate Input

number = int(input("Enter a number between: "))

while not (1 <= number <= 10):
    print("Invalid input. Please try again.")
    number = int(input("Enter a number between: "))
print("Congrats!!! Valid input received:", number)