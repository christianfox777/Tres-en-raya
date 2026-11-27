#Tres en Raya v1.0 Christian Suarez, Nicolas Rivera y Christopher Barreno
#27.09.2026
import tkinter as tk
import random
from types import SimpleNamespace


window_title = tk.Tk()
window_title.title("Tres en Raya v.1.0")
window_title.geometry("800x700")
window_title.configure(bg= "#CCE6F4")

#Seleccion modo local o modo peer to peer
def select_local_peertopeer():

    for eliminate in vars(title_items).values():
        eliminate.destroy()
    
    boton_local = tk.Button(window_title, 
                            text = "MODO LOCAL",
                            font = ("Gill Sans Ultra Bold", 20),
                            command = gameplay_tres_en_raya)
    boton_local.place(relx = 0.15, rely = 0.5)

    boton_peertopeer = tk.Button(window_title,
                                 text = "MODO ONLINE",
                                 font = ("Gill Sans Ultra Bold", 20))
    boton_peertopeer.place(relx = 0.58, rely = 0.5)

#Player selection
jugador = "X"

jugador1 = "Jugador 1"
jugador2 = "Jugador 2"
asignacion = {}  

def asignar_player(p1, p2):
    jugadores = [p1, p2]
    random.shuffle(jugadores)
    return {"x": jugadores[0], "o": jugadores[1]}

def asignacion_players():
    global asignacion
    asignacion = asignar_player(jugador1, jugador2)

def nombre_de(simbolo):
    return asignacion[simbolo.lower()]

#Matriz del juego
def gameplay_tres_en_raya():

    global jugador
    jugador = "X"                  
    asignacion_players()           
    botones = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

    congratulations_player_text_container = tk.Frame(window_title, width=400, height=200)
    congratulations_player_text_container.pack(fill="x")
    gameplay_player_container = tk.Frame(window_title, width=400, height= 400)
    gameplay_player_container.pack(fill = "x")
    
    '''
    Validar juego retorna:

    - 1 si el jugador x (1), hace 3 en raya
    - 2 si el jugador o (2), hace 3 en raya
    - None si no hay un ganador
    '''
    def validar_juego():
        for row in range(3):
            boton_row_0 = botones[row][0] 
            boton_row_1 = botones[row][1]
            boton_row_2 = botones[row][2]

            if boton_row_0.num_assign is not None and boton_row_0.num_assign == boton_row_1.num_assign and boton_row_1.num_assign == boton_row_2.num_assign:
                return boton_row_0.num_assign

        for col in range(3):
            boton_col_0 = botones[0][col]
            boton_col_1 = botones[1][col]
            boton_col_2 = botones[2][col]
                    
            if boton_col_0.num_assign is not None and boton_col_0.num_assign == boton_col_1.num_assign and boton_col_1.num_assign == boton_col_2.num_assign:
                return boton_col_0.num_assign

        boton_diag_0 = botones[0][0]
        boton_diag_1 = botones[1][1]
        boton_diag_2 = botones[2][2]

        if boton_diag_0.num_assign is not None and boton_diag_0.num_assign == boton_diag_1.num_assign and boton_diag_1.num_assign == boton_diag_2.num_assign:
                return boton_diag_0.num_assign

        boton_diag2_0 = botones[0][2]
        boton_diag2_1 = botones[1][1]
        boton_diag2_2 = botones[2][0]
        
        if boton_diag2_0.num_assign is not None and boton_diag2_0.num_assign == boton_diag2_1.num_assign and boton_diag2_1.num_assign == boton_diag2_2.num_assign:
                return boton_diag2_0.num_assign

        return None

    def deshabilitar_botones():
        for row in range(3):
            for col in range(3):
                botones[row][col].config(state = 'disabled')

    def jugar(row,col):
        print(f"{row}_{col}")

        global jugador
        boton = botones[row][col]
        if boton.cget("text")=="":
            boton.config(text = jugador)
            
            if jugador == "X":
                boton.num_assign = 1
                jugador = "O"
                print(f"El numero asignado a esa casilla es {boton.num_assign}")
                print("________________________________________________________________")

            else:
                boton.num_assign = 2
                jugador = "X"
                print(f"El numero asignado a esa casilla es {boton.num_assign}")
                print("________________________________________________________________")



            ganador = validar_juego()
            if ganador != None:
                if ganador == 1:
                    test_congratulations_player.config(text=f"{nombre_de('X')} (X) ha ganado")
                    deshabilitar_botones()
                elif ganador == 2:
                    test_congratulations_player.config(text=f"{nombre_de('O')} (O) ha ganado")
                    deshabilitar_botones()
            else:
                test_congratulations_player.config(text="No hay ganadores")

            

    def marcar_celda(boton):
        global jugador

        if boton.cget("text")=="":
            boton.config(text = jugador)
            
            if jugador == "X":
                boton.num_assign = 1
                jugador = "O"
            else:
                jugador = "X"
                boton.num_assign = 2

    test_congratulations_player = tk.Label(congratulations_player_text_container,
        text = f"{nombre_de('X')} es X y empieza | {nombre_de('O')} es O")
    test_congratulations_player.place(relx = 0.5, rely= 0.12, anchor="center")

    for row in range(3):
        for col in range(3):

            boton = tk.Button(gameplay_player_container,
                text = "",
                width=20,
                height=10,
                cursor = "cross",
                command = lambda r = row, c = col: jugar(r,c)
            )

            boton.num_assign = None
            boton.grid(row=row, column=col)
            botones[row][col] = boton

#Ventana de inicio
title_items = SimpleNamespace(

    titulo = tk.Label(window_title, text = "TRES EN RAYA", 
                        font=("Gill Sans Ultra Bold", 24), 
                        bg= "#CCE6F4", fg= "#175676"),

        text1 = tk.Label(window_title, text = "Creado por:", font = ("Arial", 12), 
                        bg= "#CCE6F4", fg= "#175676"),

        text2 = tk.Label(window_title, text = "Christian Suarez, Nicolas Rivera y Christopher Barreno", 
                        font = ("Arial", 12),
                        bg= "#CCE6F4", fg="#175676"),
    
        Begin_button = tk.Button(window_title,
                                command = select_local_peertopeer, 
                                text = "EMPEZAR", 
                                font = ("Gill Sans Ultra Bold", 20),
                                bg = "#BA324F",
                                fg= "#F3F2F2")

)

title_items.Begin_button.place(relx=0.5 , rely= 0.8, anchor="center")
title_items.text2.place(relx= 0.5, rely= 0.228,anchor="center")
title_items.titulo.place(relx = 0.5, rely= 0.12, anchor="center")
title_items.text1.place(relx = 0.5, rely= 0.18, anchor="center")

window_title.mainloop()
