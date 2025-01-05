n = 100
element = 0
sum = 0
print("Elements are:")
while n:
    if element % 2!= 0:
        print(element, end = ', ')
        sum += element
        element += 1
        n -= 1
    else:
        element += 1

print(f"\n\n Sum of first 100 odd numbers is:", sum)
