
 colors = { 'Red', 'Blue', 'Green'}

print(type(colors))                                 #Los sets son listas pero sin índice
print(colors)   

print('Red' in colors)                              #Te dice si el elemento está en la lista 
colors.add('Violet')                                #Ya que no tienen índice agregan elementos al principio y no al final
colors.remove('Blue')                               #Elimina el elemento de la lista
print(colors)

colors.clear()                                      #Elimina todos los elementos de el set
print(colors)

del colors                                          #Elimina el set
print(colors)