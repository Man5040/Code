#Una funcion es un bloque de codigo que se ejecuta cuando es llamado

def hello(name = "person"):        #Las funciones se declaran unsando def
    print('hello ' + name )

hello("Joe")
hello()                            #Si no se pone ningun valor entonces toma el valor declarado al principio

def sum(number1, number2):
    return number1 + number2

print(sum(10, 30))


add = lambda numberOne, numberTwo: numberOne + numberTwo        #Es como una funcion rapida, ya que solo se puede escribir en una sola linea

print(add(15,5))




