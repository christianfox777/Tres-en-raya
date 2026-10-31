import random

jugador1="Jugador 1"
jugador2="Jugador 2"
asignación={}

def asignar_player(p1,p2):
    jugadores=[p1,p2]
    random.shuffle(jugadores)
    return{"x":jugadores[0], "o": jugadores[1]}

def asignacion_players():
    global asignación
    asignación=asignar_player(jugador1,jugador2)

asignacion_players()
print(asignación)
print(asignación["x"], "empieza")