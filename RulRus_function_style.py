#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import randint
import os

def numeros_y_nombres_players(players, numPlay):
    for x in range(numPlay): #Lectura de jugadores y asignacion de vector de puntos
        print("Jugador", x+1)
        a = input("->")
        print("")
        players = players + [a]
        puntos.append(0)
    return players, puntos


def print_card(turn):
    if turn == 1:
        print("")
        print("Turno de", players[x])
        print("")
    f = open("%s/t%s.txt" %(direct_tarj,ran), "r", encoding="latin-1")
    print(f.read())
    f.close()
    print("")


def print_save_players_points():
    print("Puntos generados por", players[x]) #Pedido de puntos por jugador
    puntos_ronda = int(input("->"))
    puntos_totales = int(puntos[x])
    nuevos_puntos_totales = puntos_totales + puntos_ronda
    return nuevos_puntos_totales


def check_maso(tarjUsad):
    if len(tarjUsad) == numTarj:
        print("")
        print("Ya se usaron todas las tarjetas!")
        segMaz = "y"
        print("")
        baraj = input("¿Barajar el 'mazo' y seguir jugando? (y/n)")
        if baraj == y:
            tarjUsad = []
        else:
            exit()
        print("")
    else:
        segMaz = 0
    return segMaz, tarjUsad


def check_tarj_usada(tarjUsad, tarjRep):
    if ran not in tarjUsad:
        tarjUsad.append(ran)      
        print_card(0)
        tarjRep = input("¿Acaso ya te tocó esta tarjeta? (y/n)")
        print("")
    return tarjUsad, tarjRep


if __name__ == "__main__":
    direct_tarj = os.path.join(os.getcwd(),'tarjetas')
    os.chdir(direct_tarj)
    print("          _____                    _____                    _____            _____                    _____                    _____          ")
    print("         /\    \                  /\    \                  /\    \          /\    \                  /\    \                  /\    \         ")
    print("        /::\    \                /::\____\                /::\____\        /::\    \                /::\____\                /::\    \        ")
    print("       /::::\    \              /:::/    /               /:::/    /       /::::\    \              /:::/    /               /::::\    \       ")
    print("      /::::::\    \            /:::/    /               /:::/    /       /::::::\    \            /:::/    /               /::::::\    \      ")
    print("     /:::/\:::\    \          /:::/    /               /:::/    /       /:::/\:::\    \          /:::/    /               /:::/\:::\    \     ")
    print("    /:::/__\:::\    \        /:::/    /               /:::/    /       /:::/__\:::\    \        /:::/    /               /:::/__\:::\    \    ")
    print("   /::::\   \:::\    \      /:::/    /               /:::/    /       /::::\   \:::\    \      /:::/    /                \:::\   \:::\    \   ")
    print("  /::::::\   \:::\    \    /:::/    /      _____    /:::/    /       /::::::\   \:::\    \    /:::/    /      _____    ___\:::\   \:::\    \  ")
    print(" /:::/\:::\   \:::\____\  /:::/____/      /\    \  /:::/    /       /:::/\:::\   \:::\____\  /:::/____/      /\    \  /\   \:::\   \:::\    \ ")
    print("/:::/  \:::\   \:::|    ||:::|    /      /::\____\/:::/____/       /:::/  \:::\   \:::|    ||:::|    /      /::\____\/::\   \:::\   \:::\____\ ")
    print("\::/   |::::\  /:::|____||:::|____\     /:::/    /\:::\    \       \::/   |::::\  /:::|____||:::|____\     /:::/    /\:::\   \:::\   \::/    /")
    print(" \/____|:::::\/:::/    /  \:::\    \   /:::/    /  \:::\    \       \/____|:::::\/:::/    /  \:::\    \   /:::/    /  \:::\   \:::\   \/____/ ")
    print("       |:::::::::/    /    \:::\    \ /:::/    /    \:::\    \            |:::::::::/    /    \:::\    \ /:::/    /    \:::\   \:::\    \     ")
    print("       |::|\::::/    /      \:::\    /:::/    /      \:::\    \           |::|\::::/    /      \:::\    /:::/    /      \:::\   \:::\____\    ")
    print("       |::| \::/____/        \:::\__/:::/    /        \:::\    \          |::| \::/____/        \:::\__/:::/    /        \:::\  /:::/    /    ")
    print("       |::|  ~|               \::::::::/    /          \:::\    \         |::|  ~|               \::::::::/    /          \:::\/:::/    /     ")
    print("       |::|   |                \::::::/    /            \:::\    \        |::|   |                \::::::/    /            \::::::/    /      ")
    print("       \::|   |                 \::::/    /              \:::\____\       \::|   |                 \::::/    /              \::::/    /       ")
    print("        \:|   |                  \::/____/                \::/    /        \:|   |                  \::/____/                \::/    /        ")
    print("         \|___|                   ~~                       \/____/          \|___|                   ~~                       \/____/         ")
    print("                                                                                                                                              ")
    print("")
    y = "y"
    segMaz = ""
    players = []
    puntos = []
    tarjUsad = []
    numTarj = len(os.listdir("."))
    print("Cantidad de tarjetas en juego: %s" %numTarj)
    print("")
    numPlay = input("Indique el número de jugadores:")
    print("")
    numPlay = int(numPlay)

    players, puntos = numeros_y_nombres_players(players, numPlay)

    while y == "y":

        for x in range(numPlay):

            ran = randint(0,numTarj-1)
            while ran in tarjUsad: #chequeo de tarjeta usada

                ran = randint(0, numTarj-1)
                segMaz, tarjUsad = check_maso(tarjUsad)
            
            tarjUsad.append(ran) #Agregar tarjeta usada a la lista de usados      
            
            print_card(1)           
            
            if segMaz == "y": #Si ya se barajo chequear si ya salio la tarjeta al jugador

                tarjRep = input("¿Acaso ya te tocó esta tarjeta? (y/n)")
                while tarjRep == "y":

                    ran = randint(0,numTarj-1)
                    segMaz, tarjUsad = check_maso(tarjUsad)

                    tarjUsad, tarjRep = check_tarj_usada(tarjUsad, tarjRep)
            
            for x in range(numPlay):
                puntos[x] = print_save_players_points()

        print("")
        print("Los puntos de esta ronda son los siguientes:")

        for x in range(0, numPlay):
            print(players[x], puntos[x])

        y = input("¿Jugar otra ronda? (y/n)")

    print("En ese caso, los puntos finales son los siguientes:")
    for x in range(0, numPlay):
            print(players[x], puntos[x])