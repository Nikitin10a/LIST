from random import randint
a = []

for i in range(10):
    a.append(randint(1,20))
    print(a)

a.sort()
a.reverse()
print(a[0])