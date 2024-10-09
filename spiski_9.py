from random import randint
a = []
s = 0
for i in range(10):
    a.append(randint(1,20))
    print(a)

for x in a:
    s += x
    print('Сумма списка: ', s)