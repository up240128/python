#1 Declarar una lista vacía
lst = list()
print(len(lst))

#2 Declarar una lista con más de 5 elementos
lista = ['fresa', 'mango', 'pepino', 'uva', 'guayaba']
print('Los elementos que tienen son: ', len(lista))
print ('La lista de los elementos es la siguiente: ', (lista)) 

#3 Encuentra la longitud de tu lista
print('La longitud de la lista es: ', len(lista))

#4 Obtener el primer elemento, el elemento del medio y el último elemento de la lista.
fruits = ['fresa', 'mango', 'pepino', 'uva', 'guayaba']
fruits[0] = 'fresa'       
fruits[3] = 'pepino'      
fruits[4] = 'guayaba' 
print(fruits)    
print('El siguiente orden son los elementos principales, del centro y el ultimo: ', fruits[0], fruits[3], fruits[4])

#5 Declara una lista llamada mixed_data_types, coloca tu(nombre, edad, altura, estado civil, dirección)
mixed_data_types = ['Dariana', '18', '1.75', 'soltera', 'Calle de los gallos']
print('La lista de mis datos son: ', mixed_data_types)

#6 Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print ('Las compañias de it son: ', it_companies)

#7 Imprima la lista usando print()
print ('Las compañias de it son: ', it_companies)

#8 Imprima el número de empresas en la lista
print ('El numero de empresas que hay en la lista es: ', len(it_companies))

#9 Imprima la primera, la segunda y la última empresa.
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
empresas[0] = 'Facebook'       
empresas[3] = 'Apple'      
empresas[6] = 'Amazon' 
print(empresas)    
print('El siguiente orden son los elementos principales, del centro y el ultimo: ', empresas[0], empresas[3], empresas[6])

#10 Imprima el listado después de modificar una de las empresas
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
empresas [1] = 'Amazon'
empresas [0] = 'Microsoft'
print ('Las empresas modificadas son: ', empresas) 

#11 Añadir una empresa de TI a it_companies
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Samsung', 'Hp', 'Mercado libre']
print ('Las empresas modificadas son: ', empresas) 

#12 Insertar una empresa de TI en el medio de la lista de empresas
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Samsung', 'Hp', 'Mercado libre', 'intel']
empresas [5] = 'Hp'
print ('Las empresas modificadas son: ', empresas) 

#13 Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)
empresas = 'Facebook' + ' ' + ' ' + 'Google'  + ' ' + 'Microsoft' + ' '  + 'Apple' + ' ' +  'IBM' + ' ' +  'Oracle'  + ' ' +  'Amazon'
print( empresas.upper())  

#14
