import random

symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_password = []

while new_password == []:
    lenght = input("Введите длину пароля: ")
    if lenght.isdigit():
        break
    elif not lenght.isdigit():
        lenght = input('Вы ввели не число, попробуйте еще раз: ')
        if lenght.isdigit():
            break
lenght = int(lenght)
for el in range(lenght):
    new_password.append(random.choice(symbols))
print(''.join(new_password))
