# -- coding: utf-8 --
#2-var

s = str(input("Введите строку  "))
def stroka(s):
    s = s.replace(':', '%')
    return s
result = stroka(s)
print(result, result.count('%'))