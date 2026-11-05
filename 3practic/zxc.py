a = int(input())
for i in range(100, a+1):
    a1 = i // 100
    a2 = (i // 10) % 10
    a3 = i % 10
    c1 = 1
    c2 = 1
    c3 = 1
    for k in range(1, a1 +1):
        c1 = c1 * k
    for k in range(1, a2 +1):
        c2 = c2 * k
    for k in range(1, a3 +1):
        c3 = c3 * k
    if c1 + c2 + c3 == i:
        print(i)

