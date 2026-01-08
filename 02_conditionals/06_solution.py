# 6. Transportation Mode Selection

distance = int(input("Enter the distance to travel in kilometers: "))

if distance < 0:
    print("Invalid distance")
    exit()

if distance <= 3:
    mode = "walking"
elif distance <= 15:
    mode = "bike"
else:
    mode = "car"

print(f"You should use {mode} to travel.")