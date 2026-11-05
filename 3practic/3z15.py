n = int(input("Введите число N: "))

print(f"Простые числа, не превышающие {n}:")

for num in range(2, n + 1):
    
    is_prime = 1  
   
    for d in range(2, num):
        if num % d == 0:
            is_prime = 0  
            break        
            
    
    if is_prime == 1:
        print(num, end=" ")
        
