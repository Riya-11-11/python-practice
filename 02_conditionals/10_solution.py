# 10. Pet Food Recommendation

pet = input("Enter your pet type (dog/cat): ").lower()
age = int(input("Enter your pet's age in years: "))

if pet == "dog":
    if age < 2:
        food = "puppy food"
    elif 2 <= age <= 7:
        food = "adult dog food"
    else:
        food = "senior dog food"
elif pet == "cat":
    if age < 2:
        food = "kitten food"
    elif 2 <= age <= 5:
        food = "adult cat food"
    else:
        food = "senior cat food"

print(f"You should feed your {pet} with {food}.")