n = int(input("Введите число N: "))

for num in range(2, n + 1):
    div_sum = 0  
    
    
    for d in range(1, num):
        if num % d == 0:
            div_sum += d  
            
    
    if div_sum == num:
        print(num, end=" ")
