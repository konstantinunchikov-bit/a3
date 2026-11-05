n, k, r = map(int, input().split())
l = 1 + k*0.01
cnt = 1
while n <= r:
    n = n * l
    cnt += 1
print(cnt)