# SET / CONJUNTOS

#almacenan info como las listas pero no almacenan valores repetidos

numeros = {1,2,3}
print(numeros)

# intentar agregar 1 valor repetido y uno no
numeros.add(4) # lo agrega
numeros.add(1) # no lo agrega porque ya existe
print(numeros)