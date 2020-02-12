print('Hello')
#создадим список и сразу выводим его
spisok2 = ['Gosha','Max','Denis']
print(spisok2)

#Добавим в список переменную
spisok2.append('Alex')
print(spisok2)

#создадим ещё один список и добавим всё его содержимое в первый
spisok1 = ['Gordon']
spisok2.extend(spisok1)
print(spisok2)

#удаляем из списка конкретную переменную
spisok2.remove('Alex')
print(spisok2)

#удалим список
del spisok1
print('')

#разворачиваем список
print(spisok2)
spisok2.reverse()
print(spisok2)

#создадим новый список и отсортируем его
print('')
spisok = ['83','1','67']
print(spisok)
spisok.sort()
print(spisok)

#очистим этот список
spisok.clear()
print(spisok)

#выводим 1 и 3 элемент списка
print('')
str = ['gosha','alex','masha','valera']
print(str[0], str[2])


