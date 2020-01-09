a = 5
b = 2
c = a ** b   # возвожу в степень
print(c)

'''
комментируем блоками
'''
# комментируем стоку (можно нажать также: CTRL+/)

# PEP 8

# ТИПЫ ДАННЫХ

a = 10 # (Int) целое число
b = 'Petrov' # ('Str') строковый тип данных
c = 200.10 # (float) число с плавающей точкой

# посмотреть тип переменной
print(type(a))
print(type(b))
print(type(c))

# булевые типы данных 'bool' - либо да, либо нет (True/False)
is_admin = True
is_user = False
print(type(is_admin))
print(type(is_user))

# тип данных - 'list' - СПИСОК []
people = ['qwe', 'asd', 'zxc']
print(type(people))
print(people)
people = [a, b, c, is_admin, is_user]
print(people)
# элементы списка начинаются с нуля; и если в обратном порядке то: с -1 (первый с конца)
print(people[1])
print(people[-1])

# вложенный список
people = [a, b, c, is_admin, is_user, [5, 2]]
print(people)
# чтобы достать элемент из вложенного списка
print(people[5] [1]) # достанет из списка цифру 2

# добавить в конец списка
people.append('Валерия') # добавили в конец списка имя Валерия - шестым элементом
print(people)

# тип данных - 'tuple' - КОРТЕЖ () - неизменяемый список
people = (a, b, c, is_admin, is_user, [5, 2])
print(type(people))
print(people)
# отличие кортежа от списка - скобки; - кортеж нельзя изменить

# тип данных - 'dictionary' - СЛОВАРЬ {}
human = {'name': 'Ivan', 'age': 30} # ключ : значение
print(type(human))
print(human)
print(human['age'])

# если типы данных разные
a = 100
b = '1' # строку перевести в тип Int
print(a + int(b))

# или наоборот перевести в строку
print(str(a) + b) # тогда мы склеим две строки - конкатинация - 1001

# если число с плавающей точкой
a = 100
b = '1.1' # строку перевести в тип float
print(a + float(b)) # выдаст ответ с дробной частью: 101.1

print(a + int(float(b))) # выдаст ответ с отсеченной дробной частью: 101

# Запрос данных от пользователя
'''name = input('Ваше имя: ')
print('Привет, ', name+'!')


age = int(input('Ваш возраст: ')) # если надо дробное число: age = float(int(input('Ваш возраст: ')))
print('Через 10 лет Вам будет: ', age + 10)
'''

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ СРАВНЕНИЯ
'''
print(5 > 1) # True
print(5 < 1) # False
print(5 == 1) # False - операция сравнения - равенство
print(5 != 1) # True - операция сравнения - неравенство (разные ли они по значению)
print(5 == 5.0) # True - int и float - будут равны
# <= меньше или равно
# >= больше или равно
'''

print(bool(0)) # False - 0 или пустота ''- всегда False
print(bool(1)) # True - 1 или любое значение - всегда True - переводим в булево значение - истина или ложь

# программка
'''
price = 100
money = int(input('Сколько денег есть: '))

if money >= price:
    print('Мы можем это купить')
elif price - money <= 5:
    print('Можем поторговаться')
else:
    print('Денег не хватает')
    
    
name = input()
if name:
    print('Имя введено')
else:    
    print('Пусто')
'''

'''
name = input('Name: ')
surname = input('Surname: ')

if name and surname:
    print('Все введено')
elif name or surname:
    print('Вы не ввели фамилию или имя')
else:
    print('Ничего не ввели')
'''

# ЦИКЛ While (цикл - делай какое либо действие - пока условие - истина)

'''
number = int(input('Введи число от 1 до 5: '))

while number < 1 or number > 5:
    print('Введено не верное число')
    number = int(input('Введи число от 1 до 5: '))
'''

'''
x = 0

while x <= 10:
    print(x)
    if x == 8:
        break  # прервет программу когда х будет равен 8
    x += 1 # увеличит х на 1
'''

'''
x = 0
while x <= 10:
    x += 1  # увеличит х на 1
    if x == 9:
        break
    elif x == 4:
        continue # пропустит 4
    print(x)
'''











