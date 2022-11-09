# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Empecemos a jugar con las listas y su métodos, el objetivo
es realizar el código lo más simple, ordenado y limpio posible,
no utilizar bucles donde no haga falta, no "re inventar" una función
que ya dispongamos de Python. El objetivo es:

1) Generar una lista de 3 numéros aleatorios con random (pueden repetirse),
    estos 3 nuḿeros deben estar comprendidos entre 1 al 10 inclusive.
2) Luego de generar la lista sumar los números y ver si el resultado
    de la suma es menor o igual a 21
    a) Si el número es menor o igual a 21 se imprime en pantalla
        la suma y los números recoletados
    b) Si el número es mayor a 21 se debe informar al usuario que perdio
'''
import random
import numpy as np

if __name__ == '__main__':
    print('Comenzamos a divertirnos!')
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

    listita= [random.randint(1,10) for x in range(3)]
    arraycito = np.asanyarray(listita)
    sumita = np.sum(arraycito)
    if sumita <= 21:
        print("La suma de sus números es",sumita)
        print("Los números recolectados son",listita)
    else:
        print("Te pasaste de 21, has perdido TODO!!! 💀")
    
    print("Terminamos")