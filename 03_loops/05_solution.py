# 5. Find the First Non-Repeated Character

characters = "interesting"
for char in characters:
    if characters.count(char) == 1:
        print("First non-repeated character:", char)
        break
