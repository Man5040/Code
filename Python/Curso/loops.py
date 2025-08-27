#Existen 2 tipos de loops en python

foods = ['apples', 'banana', 'bread', 'cheese', 'eggs', 'grapes/']

#Loop for
for food in foods:                      #El loop for itera los elementos de la lista
    print(food)


for food in foods:
    if food == "banana":
        continue                        #EL continue sirve para continuar, pero se salta el elemento, porque hace la validacion, y por lo tanto sigue con el siguiente elemento
    if food == "cheese":
        break                           #El break sirve para romper el loop                 
    print(food)        
        
for number in range(1,8):
    print(number)    

for letter in 'hello':                  #Si tienes un string, cuenta cada letra como un elemento de una lista
    print(letter)


#Loop while

count = 4

while count <= 10:                      #El loop count continua hasta que no se cumpla la condicion
    print(count)
    count = count + 1 



