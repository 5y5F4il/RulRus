from random import randint
import os
direct_tarj = os.path.join(os.getcwd(),'tarjetas')
os.chdir(direct_tarj)
print("")
print("Bienvendio a RulRus!")
print("")
print("Proximamente un buen logo aquí!")
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
for x in range(numPlay): #Lectura de jugadores y asignacion de vector de puntos
    print("Jugador", x+1)
    a = input("->")
    print("")
    players = players + [a]
    puntos.append(0)
while y == "y":
    for x in range(numPlay):
        ran = randint(0,numTarj)
        while ran in tarjUsad: #chequeo de tarjeta usada
            ran = randint(0, numTarj)
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
        tarjUsad.append(ran) #Agregar tarjeta usada a la lista de usados
        print("")
        print("Turno de", players[x])
        print("")
        f = open("%s/t%s.txt" %(direct_tarj,ran), "r")
        print(f.read())
        f.close()
        print("")
        if segMaz == "y": #Si ya se barajo chequear si ya salio la tarjeta al jugador
            tarjRep = input("¿Acaso ya te tocó esta tarjeta? (y/n)")
            while tarjRep == "y":
                ran = randint(0,numTarj)
                if len(tarjUsad) == numTarj:
                    print("")
                    print("Ya se usaron todas las tarjetas!")
                    print("")
                    baraj = input("¿Barajar el 'mazo' y seguir jugando? (y/n)")
                    if baraj == y:
                        tarjUsad = []
                    else:
                        exit()
                print("")
                if ran not in tarjUsad:
                    tarjUsad.append(ran)
                    f = open("%s/t%s.txt" %(direct_tarj,ran), "r")
                    print(f.read())
                    f.close()
                    print("")
                    tarjRep = input("¿Acaso ya te tocó esta tarjeta? (y/n)")
                    print("")
        for x in range(numPlay):
            print("Puntos generados por", players[x]) #Pedido de puntos por jugador
            puntos_ronda = int(input("->"))
            puntos_totales = int(puntos[x])
            nuevos_puntos_totales = puntos_totales + puntos_ronda
            puntos[x] = nuevos_puntos_totales
    print("")
    print("Los puntos de esta ronda son los siguientes:")
    for x in range(0, numPlay):
        print(players[x], puntos[x])
    y = input("¿Jugar otra ronda? (y/n)")
print("En ese caso, los puntos finales son los siguientes:")
for x in range(0, numPlay):
        print(players[x], puntos[x])