
cart = {

        'name'      : 'book',
        'quantity'  :  3    ,
        'price'     :  4.99

}                                   #Sirve para categorizar cosas en las listas

person = {

        'first_name':  'ryan',
        'last_name' :  'ray'
}

print(type(person))
print(dir(person))                  #Sirve para ver que se puede hacer con la variable
print(person.keys)                  #Sirve para ver los elementos de la parte izquierda ya que estos se llaman keys
print(person.items)                 #Nos enseña la variable
print(person)
person.clear()                        #Vacia la variable
print(person)

del person                          #Sirve para eliminarlo

products = [
        {'name': 'book','price': 2.99},
        {'name': 'laptop', 'price': 10000}      #Se pueden tener varios dictionaries a la vez
]

print(products)