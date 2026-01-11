# 2. Sum of for Even Numbers
 
n = 10
sum_even = 0
for i in range(1, n):
    if i % 2 == 0:
        print("Even number:", i)
        sum_even += i
print("Sum of even numbers:", sum_even)