n = int(input("Введите максимальное число точек N: "))
total_dots = 0

for i in range(0, n + 1):

    for j in range(i, n + 1):
        
        total_dots += (i + j)

print("Суммарное количество точек:", total_dots)
