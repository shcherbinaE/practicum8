a = input()
while a.isdigit() == False:
    a = input('Ошибка. Попробуйте еще раз. Введите число: ')
print('Введено целое число:', a)