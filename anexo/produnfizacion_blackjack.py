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
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''
import random



if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    

   

    def black_jack(jugador1,jugador2,mano1,mano2,turno):
   
        while turno == 0:
            if mano1 == 0:
                print("Turno de ", jugador1)
                mano1 = [random.randint(1,10) for x in range(2)]
                total1 = sum(mano1)

            else:
                total1 = sum(mano1)
                if total1 > 21:
                    print("El total de ", jugador1, " es de ", total1,". Se exedió de los 21, gana la mano ", jugador2,".")
                    exit()
                else:
                    print("Su total es ", total1, "ingrese ", '\033[1m' + "carta" + '\033[0m', " si quiere otra carta o", '\033[1m' + "quedarse" + '\033[0m', "si se quiere quedar" )
                    elección = input()
                    if elección == "carta":
                        mano1.append(random.randint(1, 10)) 
                    elif elección == "quedarse":
                        turno = 1
                        continue
        while turno == 1:
            if mano2 == 0:
                print("Turno de ", jugador2)
                mano2 = [random.randint(1,10) for x in range(2)]
                total2 = sum(mano2)

            else:
                total2 = sum(mano2)
                if total2 > 21:
                    print("El total de ", jugador2, " es de ", total2,". Se exedió de los 21, gana la mano ", jugador1,".")
                    exit()
                else:
                    print("Su total es ", total2, "ingrese ", '\033[1m' + "carta" + '\033[0m', " si quiere otra carta o", '\033[1m' + "quedarse" + '\033[0m', "si se quiere quedar" )
                    elección = input()
                    if elección == "carta":
                        mano2.append(random.randint(1, 10)) 
                    elif elección == "quedarse":
                        turno = 2
                        continue
        while turno == 2:
            if total1 == total2:
                print("ambos jugadores tienen el mismo puntaje, nadie gana... ¯\_(ツ)_/¯ ")
                exit()
            elif total1 > total2:
                print("El total de ", jugador1, " es de ", total1,", el de ", jugador2, " es ", total2, " .", jugador1, " es el ganador. " )
                exit()
            elif total2 > total1:
                print("El total de ", jugador2, " es de ", total2,", el de ", jugador1, " es ", total1, " .", jugador2, " es el ganador. " )
                exit()
            

 #Se lo muestra a los jugadores junto a la Bienvenida y se les pide que ingresen sus nombre.
    
    print("Para comenzar la experiencia ambos jugadores deben ingresar sus nombres.")
    nombre1 = input("Por favor ingrese el nombre del primer jugador: ")
    nombre2 = input("Por favor ingrese el nombre del segundo jugador: ")

    # Se selecciona al jugador que empezará primero, aleatoriamente.
    if random.choice([1,2]) == 1:
        jugador1 = nombre1
        jugador2 = nombre2
    else:
        jugador1 = nombre2
        jugador2 = nombre1

    mano1 = 0
    mano2 = 0
    turno = 0

    black_jack(jugador1,jugador2,mano1,mano2,turno)
