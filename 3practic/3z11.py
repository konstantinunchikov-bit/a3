max_attemp = 0

while True:
    t = int(input())
    if t == -1:
        break
      
    if t > max_attemp:
        max_attemp = t
print(max_attemp)

