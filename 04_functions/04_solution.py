# Create a function that returns both the area and circumference of a circle given its radius.

import math
def circle_properties(radius):
    area = round(math.pi * (radius**2), 2)
    circumference = round(2 * math.pi *radius, 2)
    return area, circumference

area, circumference = circle_properties(5)
print(f"Area: {area}, Circumference: {circumference}")