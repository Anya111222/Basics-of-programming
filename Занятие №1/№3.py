# -- coding: utf-8 --
name = str(input())
age = int(input())
if age >= 16:
    print('Поздравляем вы поступили в ВГУИТ')
else:
    print('Сначала нужно окончить школу!')
if 0 < age < 75:
    print(age)
if name != 'Иван':
    print(name)
if age < 16:
    print(16-age)