# 4. Fruit Ripeness Checker

fruit = "banana"
color = input("Enter the color of the banana (yellow, green, brown): ").lower()

if fruit == "banana":
    if color == "yellow":
        print("The banana is ripe.")
    elif color == "green":
        print("The banana is unripe.")
    elif color == "brown":
        print("The banana is overripe.")
