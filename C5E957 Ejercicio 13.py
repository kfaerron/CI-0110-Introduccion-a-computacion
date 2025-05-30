'''
 Ejercicio 13 - Actividad 4 

Propósito: Crear una lista con 15 números aleatorios entre 1 y 100, para luego pedir al usuario un número:
si el número indicado por el usuario está en la lista, el usuario “ganó” el juego y se le debe indicar la posición
en que se encontró; si no adivina el número después de tres intentos, se le muestran todos los valores
contenidos en la lista.

1.  lista <-- []
2.  num_aleatorio <-- generar numero aleatorio (1,100)
3.  i <-- 1
4.  while i <= 3 then
4.1    numero <-- pedir al usuario
4.1    if numero in lista then
4.1.1    print <-- "ganaste"
4.1.1    posicion <-- indice + 1
4.1.1    print <-- "el numero fue encontrado en la posición", posicion
4.1.1    break 
4.2   else
4.2.1    i <-- i + 1
4.3    if i == 4
4.3.1    print <-- lista


'''
#Se importa la libreria
import random as rn

i = 1

#lista vacia
lista = []

#Se crean los números y se añaden a lista
for n in range (15):
    num_aleatorio = rn.randint(1, 100)
    lista.append(num_aleatorio)
    
#Se le pide al usuario el número y se verifica      
while i <= 3:
    numero = int(input("Digita un número del 1 al 100: "))
    print()
    if numero in lista:
        print("Ganaste") 
        posicion = lista.index(numero)         #<--Se busca la posición del número
        posicion = posicion + 1
        print(f"El número fue encontrado en la posición {posicion}")
        break
    else:
        i += 1
    if  i == 4:
        print(f"La lista contenía estos números {lista}")  #<-- el usuario pierde 
     
