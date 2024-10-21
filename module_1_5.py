# Изменяемые и неизменяемые объекты. Кортежи
immutable_var = 1,2,3,'4'
print ('Immutable tuple:', immutable_var)
# immutable_var[1] = 8 не выполняется
mutable_list = [1,2,3,'4','5']
mutable_list [4] = 6
print('Mutable list:', mutable_list)
