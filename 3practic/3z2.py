a = input()
b = len(a)
c = ''
for i in range(0,b):
    if i % 3 == 2:
        c += a[i]
print(c)

