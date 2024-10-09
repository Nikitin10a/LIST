from random import randint

a = []
s = 0
t = 0

for i in range(10):
    a.append(randint(1,20))
    print(a)

for x in a:
    s += x
    t += x/x
    print('Среднее арифметическое', s/t)