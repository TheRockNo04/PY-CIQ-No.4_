import random

array = [random.randint(-5,10) for x in range(15)]
array.sort()
a = 0
print(array)

for i in range(len(array)+1):
    if i > 0:
        if not a in array:
            print(f"{a} is not in the list")
            break
        else:
            a += 1