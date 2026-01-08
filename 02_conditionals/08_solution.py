# 8. Password Strength Checker

password = input("Enter your password: ")
length = len(password)

if length < 6:
    strength = "weak"
elif 6 <= length <= 10:
    strength = "medium"
else:
    strength = "strong"

print(f"Your password is {strength}.")