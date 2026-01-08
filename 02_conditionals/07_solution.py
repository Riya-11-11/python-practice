# 7. Coffee Customization

coffee_size = input("Enter coffee size (small, medium, large): ").lower()
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").lower()

if extra_shot == "yes":
    print(f"coffee {coffee_size} + extra shot")
else:
    print(f"coffee {coffee_size}")