vvod = input().split()
if len(vvod) != 3:
    print("Ошибка: введите пример в формате '5 + 3'")
    exit() # Завершаем работу
a = int(vvod[0])
op = vvod[1]
b = int(vvod[2])
# Проверяем, что числа в диапазоне от 1 до 10
if a < 1 or a > 10 or b < 1 or b > 10:
    print("Ошибка: числа должны быть от 1 до 10")
    exit()
# Считаем результат в зависимости от знака
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a // b)
else:
    # Если знак не +, -, * или /
    print("Ошибка: неверная операция")
    exit()