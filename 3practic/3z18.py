x = int(input("Введите натуральное число x: "))
count = 0


for a in range(1, x):
    if a * a > x:
        break
        
    for b in range(a, x):
        current_sum = a * a + b * b
        
        if current_sum == x:
            count += 1
            break  
        elif current_sum > x:
            break  

print("Количество способов:", count)
