nombre1 = input ("¿Como se llamara el jugador 1? ")
nombre2 = input ("¿Como se llamara el jugador 2? ")

jugador1 = input("¡Hola Jugador 1! ¿Qué eliges? ¿Piedra, Papel o Tijeras?: ")
jugador2 = input("¡Hola Jugador 2! ¿Qué eliges? ¿Piedra, Papel o Tijeras?: ")

condicion1=jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1  == jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print ("Victoria de", nombre1)
else:
    print ("Victoria de", nombre2)