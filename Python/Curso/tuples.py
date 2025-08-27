x = (1, 2, 3)                   #Se puede crear una tuple ya sea con la funcion tuple  simplemente escribiendo las cosas entre parentesis
y = tuple((1, 2, 3))            #"x = y"

z = (1)                         #Si solo tenemos un elemeto en la tuple se considera como solo ese elemento (es decir no es una tuple)
print(z) 
print(type(z))

z= (1,)                         #Si queremos una tuple de un solo elemento debemos usar una coma
print(z)
print(type(z))

del z                           #Elimina la tuple

print(dir(x))                   #Nos da las opciones que podemos hacer con las tuples
print(x[2])                     #Nos dice el elemento en la posición seleccionada

locations = {
    (155, 39.23) : "Tokyo",     #Los dictionaries tambien pueden estar en las tuples
    (140, -42.9) : "New York"
}

print(locations)