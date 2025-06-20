lenguajes = ["Python","Ruby","PHP","JS","Java"]
lenguajes.insert(0,"Go") # Insertar elemento en un indice especifico
lenguajes.append("HTML") # insertar al final
lenguajes.remove("Python") # Eliminar elemento ( enviar el valor a eliminar )
lenguajes.pop(4) # Eliminar un elemento pero con el indice, elimina java
print(len(lenguajes)) # Contar elementos en una lista 



print(lenguajes)
print("Go" in lenguajes) # Validar si existe un str en la lista ( respuesta boleano)