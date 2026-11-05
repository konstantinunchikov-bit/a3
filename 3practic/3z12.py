k = int(input("Введите K: "))
current_sum = 0
expression = ""

for i in range(1, k + 1):
    current_sum += i
    if i == 1:
        print(1)
    else:
        print(current_sum)

