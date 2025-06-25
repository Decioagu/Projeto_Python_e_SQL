lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
lista3 = []

zip_object = zip(lista1, lista2) # retorna um objeto Map
print(zip_object) # <zip object at 0x000001A2B3C4D5E6>

for item in zip_object:
    lista3.append(item)

print(lista3) # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#  OU

lista3 = [valor for valor in zip_object]  
print(lista3) # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

print()