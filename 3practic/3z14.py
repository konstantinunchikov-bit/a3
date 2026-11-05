
user_input = input("Введите число: ")


while not user_input.isdigit():
    
    user_input = input("Ошибка. Попробуйте еще раз. Введите число: ")


print("Введено целое число:", user_input)
