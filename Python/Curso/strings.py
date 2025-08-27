myStr= "hello world"

print(dir(myStr))
print(len(myStr))                               #Sirve para contar el númer de caracteres

print(myStr.upper())                            #Pone todo en mayúsculas
print(myStr.lower())                            #Pone todo en minúsculas
print(myStr.swapcase())                         #Intercala mayúscula y minusculas
print(myStr.capitalize())                       #Pone la primer letra mayúscula
print(myStr.replace("hello", "bye").upper())    #Remplaza la palbra
print(myStr.count("l"))                         #Cuenta
print(myStr.startswith("hello"))                #Detecta si empieza por una palabra
print(myStr.endswith("ld"))                     #Detecta si termina con esos caractere
print(myStr.split("o"))                         #Hace una lista donde se separa el texto dependiendo de la letra
print(myStr.find("o"))                          #Te da la posición de la letra en el texto
print(myStr.index("e"))                         #Te da la posición de la letra en el texto empezando desde el 0
print(myStr.isnumeric())                        #Te dice si es un número
print(myStr.isalpha())                          #Te dice si es alfanumerico
print(myStr[4])                                 #Te da la letra en la posicion 4
print(myStr[-1])                                #Si los números son negetibos empieza por el final

print("My name is " + myStr)                    #Se puede concatenar textos de ambas formas
print(f"My name is {myStr}")                    #La f hace que detecte que lo que esta detro de las llaves se detecte como variable









