
colors = ["red", "blue", "green"]

number_list = list((1, 2, 3, 4))                      #Se crea una tuple porque la variable solo acepta una entrada y no todos los elementos de la lista
r= list(range(1, 100))                                #Ramge crea una lista del primer numero hasta n-1, osea el antecesor del ultimo numero
print(r)

print(dir(colors))                                    #Te da las funciones que puedes hacer con la lista
print(len(colors))                                    #Te dice cuantos elementos hay en la lista
print(colors[0])                                      #Te da el elemento que este en la poscicion que le dijiste
print("green" in colors)                              #Te dice si el elemento esta en la lista

print(colors)

colors.sort()                                         #Cambia de orden a la lista
print(colors) 

colors.sort(reverse=True)                             #Cambia de orden a la lista
print(colors) 

colors[1] = "yellow"                                  #Reemplaza el elemento de la lista
colors.append("violet")                               #Agrega un elemento a la lista
colors.append(("orange" , "black"))                   #Solo acepta un elemento, pero es posible agregar varios en forma de lista
colors.extend(("white", "pink"))                      #Extend agrega la lista en forma de elementos (sin los paraentesis)
colors.insert(3, "purple")                            #Agrega los elementos el lugar seleccionado
colors.insert(len(colors), "gray")                    #Como len te da el numero de elementos, lo inserta al final de la tuple
print(colors)

colors.pop()                                          #Elimina el ultimo elemento de la lista o el que este en la posicion elegida
colors.remove("blue")                                 #Elimina el elemento por nombre
print(colors) 

print(colors.index("yellow"))                         #Te dice el lugar en el que esta el elemento
print(colors.count("red"))                            #Te dice cuantas veces se repite el elemento

colors.clear()                                        #Vacia la lista
print(colors) 


