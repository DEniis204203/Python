#создаём кортедж
row = ('Denis', 'Stepan2', 'Tramp')
print(row)

#с помощью tuple создаём пустой кортедж
row2 = tuple()
print(row2)

#создаём множество и удаляем лишние знаки
digits = [0,1,1,1,2,3,6,5,4,6,4,5,4,4]
print(set(digits))

#проверяем наличие цифры 6 и 46 в множестве
digits_set = set(digits)
print(6 in digits_set)
print(46 in digits_set)

#вычитание в массивах
even = {1,6,5,4,3}
goshan = digits_set - even
print(goshan)
print()

#операция возвращает элементы присутствующие в обоих массивах
prime = {1,2,13,15,23}
prime_even = prime & even
print(prime_even)

#создаём множество и удаляем лишние  имена
print('Проверка со словами')
digits = ['Denis','Stepan','Andrey','Andrey']
print(set(digits))
digits_set = set(digits)
#проверяем наличие цифры слова Andrey и Gosha множестве
print('Andrey' in digits_set)
print('Gosha' in digits_set)
#вычитание имен в массивах
even = {'Andrey', 'Stepan'}
goshan = digits_set - even
print(goshan)
#операция возвращает элементы присутствующие в обоих массивах
prime_even = digits_set & even
print(prime_even)








