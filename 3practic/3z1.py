a = []
cnt = 0
for i in range(100, 1000):
    if i % 17 == 0:
        a += [i]
        cnt += 1
print(a)
print(cnt)