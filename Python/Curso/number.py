
#Python sigue jerarquia de operaciones

print(type(1))                                 #integer
print(type(1.0))                               #float     
print(type(1 + 1.0))                           #si se suma un int + float te devuelve un float
print(2**3)                                    #significa 2 elevado a 3
print(11//3)                                   #te da el resultado int de la division
print(11 % 3)                                  #te da el residuo de la division

age = input("Insert your age:" )               #La funcion input sirve para escribir cosas
new_age = int(age) -2                          #La funcion input devuelve un string, y con int se camba a integer
print(new_age)