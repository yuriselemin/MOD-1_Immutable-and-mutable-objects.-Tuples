
# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"



# 1 Кортеж

immutable_var = 1,2,3,4,'кортеж',True,[8,9,10]
print(immutable_var)

immutable_var[6][1] = 'яблоко'
print(immutable_var)          # в данном случае заменить можно только элементы внутри списка который находится в кортеже
immutable_var[4] = ['яблоко']
print(immutable_var)          # неудалось заменить строку списком так как кортеж является неизменяемым типом данных




# 2 Список

mutable_list = ['Москва', 'Владивосток', 'Тверь', 'Ялта']

print(mutable_list)                 # изменение списка срезом
mutable_list[3] = 'нейросеть'
mutable_list[2] = 'программинг'
mutable_list[1] = 'усидчивость'
mutable_list[0] = 200
print(mutable_list)
mutable_list = mutable_list[::-1]
print(mutable_list)
mutable_list = mutable_list[::-1]
print(mutable_list)
                                    # изменение списка через методы
mutable_list.append(10)             # - append
print(mutable_list)
mutable_list.extend('код')          # - extend
print(mutable_list)
mutable_list.extend(['код'])
print(mutable_list)
mutable_list.remove(200)            # - remove
print(mutable_list)
