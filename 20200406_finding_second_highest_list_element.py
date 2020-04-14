import random
array=[]
for i in range(1,random.randint(1,100)):
    array.append(random.randint(1,100))

print(array)
max=0
prevmax=None
for i in array:

    if i > max:
        prevmax=max
        max=i

print(prevmax,max)
