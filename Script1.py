import random

def imprimir_marcador(marcador, j1, j2):
    print(f"Jugador 1 ({j1}) \t Sets: {marcador['sets1']} \t Juegos: {marcador['juegos1']} \t Puntos: {marcador['puntos1']}\n"
          f"Jugador 2 ({j2}) \t Sets: {marcador['sets2']} \t Juegos: {marcador['juegos2']} \t Puntos: {marcador['puntos2']}\n")

def anotar_punto(marcador, jugador, contrincante, juegos, j):
    global saque_actual
    global jugador1
    global jugador2
    if marcador[jugador] == 0 or marcador[jugador] == 15:
        marcador[jugador] += 15
    elif marcador[jugador] == 30:
        marcador[jugador] += 10
    elif marcador[jugador] == 40 and marcador[contrincante] == 40:
        marcador[jugador] = 'ventaja'
    elif marcador[jugador] == 40 and marcador[contrincante] == 'ventaja':
        marcador[contrincante] = 40
    else:
        marcador[jugador] = 0
        marcador[contrincante] = 0
        marcador[juegos] += 1
        print(f"\n¡{j} ha ganado el juego!\n")
        saque_actual = jugador2 if saque_actual == jugador1 else jugador1
        if (marcador['juegos1'] + marcador['juegos2']) % 2 == 1:
            print(f"\n¡Cambio de cancha!\n")
        print(f"\n¡{saque_actual} sacará!\n")
        

def anotar_set(marcador, jugador1, jugador2):
    if marcador['juegos1'] >= 6 and marcador['juegos1'] >= marcador['juegos2'] + 2:
        marcador['sets1'] += 1
        marcador['juegos1'] = 0
        marcador['juegos2'] = 0
        print(f"\n¡{jugador1} ha ganado el set!\n")
    elif marcador['juegos2'] >= 6 and marcador['juegos2'] >= marcador['juegos1'] + 2:
        marcador['sets2'] += 1
        marcador['juegos1'] = 0
        marcador['juegos2'] = 0
        print(f"\n¡{jugador2} ha ganado el set!\n")


marcador = {'sets1' : 0, 'sets2' : 0,
            'juegos1' : 0, 'juegos2' : 0,
            'puntos1' : 0, 'puntos2' : 0}

jugador1 = input("Ingrese el nombre del Jugador 1: ")
jugador2 = input("Ingrese el nombre del Jugador 2: ")

saque_actual = random.choice([jugador1, jugador2])
print(f"\n¡{saque_actual} sacará primero!\n")

while True:

    anotar_set(marcador, jugador1, jugador2)
    
    imprimir_marcador(marcador, jugador1, jugador2)
    
    ganador = None
    if marcador['sets1'] >= 2:
        ganador = jugador1
    elif marcador['sets2'] >= 2:
        ganador = jugador2

    if ganador:
        print(f"\n¡{ganador} ha ganado el partido!")
        break

    try:

        jugador_que_anota = input("\n¿Quién anota punto? (Ingrese el nombre del jugador) ")

        if jugador_que_anota == jugador1:
            anotar_punto(marcador, 'puntos1', 'puntos2', 'juegos1', jugador_que_anota)
        elif jugador_que_anota == jugador2:
            anotar_punto(marcador, 'puntos2', 'puntos1', 'juegos2', jugador_que_anota)

        else:
            raise ValueError('jugador no valido, ingresa el nombre del jugador 1 o del jugador 2 \n')

    except ValueError as e:
        print(f'\nError: {e}')
    
        

