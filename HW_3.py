# Task 1
## из целых в дробные
i = 5
while i > 0:
    a = int(input('Введите целое число '))
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', float(a), 'его тип:', type(float(a)), '\n')
    i -= 1

## из дробных в целые
i = 5
while i > 0:
    a = float(input('Введите дробное число '))
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', int(a), 'его тип:', type(int(a)), '\n')
    i -= 1

## из целого в строку
i = 5
while i > 0:
    a = int(input('Введите целое число '))
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', str(a), 'его тип:', type(str(a)), '\n')
    i -= 1

## из дробного в строку
i = 5
while i > 0:
    a = float(input('Введите дробное число '))
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', str(a), 'его тип:', type(str(a)), '\n')
    i -= 1

## из строки в целое
i = 5
while i > 0:
    a = input('Введите число ')
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', int(float(a)),
          'его тип:', type(int(float(a))), '\n')
    i -= 1

## из строки в дробное
i = 5
while i > 0:
    a = input('Введите число ')
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', float(a), 'его тип:', type(float(a)), '\n')
    i -= 1

# Task 2. Таблица истинности
oper = input('введите операцию, таблицу истинности для которой Вы хотите получить ')
print('   ', oper+':')
if oper == 'not':
    print("T   ->", not(True), "\n"+"F   ->", not(False))
elif oper == 'or':
    print("T,T   ->", True or True, "\n"+"T,F   ->", True or False,
          "\n"+"F,T   ->", False or True, "\n"+"F,F   ->", False or False)
elif oper == 'xor':
    print("T,T   ->", "False", "\n"+"T,F   ->", "True"
                                                "\n"+"F,T   ->", "True", '\n'+"F,F   ->", "False")
elif oper == 'nor':
    print("T,T   ->", "False", "\n"+"T,F   ->", "False"
                                                "\n"+"F,T   ->", "False", '\n'+"F,F   ->", "True")
elif oper == 'and':
    print("T,T   ->", True and True, "\n"+"T,F   ->", True and False,
          "\n"+"F,T   ->", False and True, "\n"+"F,F   ->", False and False)
elif oper == 'nand':
    print("T,T   ->", "False", "\n"+"T,F   ->", "True"
                                                "\n"+"F,T   ->", "True", '\n'+"F,F   ->", "True")

# Task 3. Вариация старой задачки fizzbuzz - сделайте программу, на вход которой поступает целое число,
# если это число делится на 3 выводится fizz, если на 5 - buzz,
# а если на 15 - fizzbuzz. Если не делится нацело ни на одно из них, выведите это же число (8 баллов)

number = int(input('Введите целое число '))
if number%3 == 0 and number%5 != 0:
    print("fizz")
elif number%3 != 0 and number%5 == 0:
    print("buzz")
elif number%15 == 0:
    print("fizzbuzz")
else:
    print(number)