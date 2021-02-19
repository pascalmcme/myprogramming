

list = ["a","b","c"]  #changeable and orderable collection


tuple = (2,3) # not changeable
print(type(list))
print(len(tuple))

list.append(99)

print(list)

newlist = list + [1]
print(newlist)

lista = [1,2,'a',True]  # different data types in list


print(lista[0])
print(lista[1:])  # 1 to end
print(lista[::-1])
print(lista[::2]) #note we start counting at 0

x = lista.pop(0)
print(x)