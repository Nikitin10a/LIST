l = str(input("Введите строку: "))

b = []

for i in l:
    b.append(i)
print(b)

if 'a' in b:
    b.remove('a')
elif 'e' in b:
    b.remove('e')
elif 'o' in b:
    b.remove('o')
else:
    pass
print(b)