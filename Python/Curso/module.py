#Existen 3 tipos de modulos, los que ya tiene python, los que se descargan de internet
# y los que creas tu mismo

#python modules

import datetime                     #Para usar un codigo lo tenemos que primero importar
                                    #Podemos buscar los modulos en "Python module index"

print(datetime.date.today())
print(datetime.timedelta(minutes=100))

from datetime import timedelta, date      #Podemos importar directamente los metodos y de esta forma no tenemos que poner el datetime. del principio
print(timedelta(minutes=60))
print(date.today())


#Own Modules

import fmath

fmath.add(1,2)
fmath.substract(2,1)


#Third party modules                #Se buscan en "pip python"
#Se instalan poniendo pip mas el codifo de el modulo
#Ejemplo "pip install colorama"

import colorama
print(colorama.Fore.RED + "Hello World")