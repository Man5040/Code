
x   =   10

if x < 30:
    print('x is less than 30')             #Se suele poner un tab o un espacio antes de la indicacion del if
else:                                      #Es lo que ocurre si la condicion no se cumple
    print('x is greater than 30')       

y   =   10
x == y                                     #Sirve para comprobar si son iguales
print(x == y)

x   =   30

if x == 30:                                #Siempre se usa == ya que = sirve para declarar variables
    print('x is equal to 30')


colors = 'blue'                            #Tambien funciona con strings
if colors == 'red':
    print('red')
elif colors == 'blue':                     #Es un caso particular que funciona como otro if en caso de que el primero sera falso pero el siguiente sea verdadero
    print('blue')
else:
    print('any color')


name = 'Jhon'
lastname = 'Carter'
if name == 'Jhon':
    if lastname == 'Carter':
        print('You are Carter')
    else:
        print('You are not Carter')
else:
    print('You are not Jhon')

if x > 2 and x <= 10:
    print('x is grater than 2 and less or equal to ten')
if x < 2 or x >= 10:
    print('x is less than 2 or greater or equal to 10')
if (not(x == y)):
    print('x is not equal to y')