import tkinter as tk

root = tk.Tk()
root.title("Prueba de botones de x y o")
botones = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

congratulations_player_text_container = tk.Frame(root, width=400, height=200)
congratulations_player_text_container.pack(fill="x")
gameplay_player_container = tk.Frame(root, width=400, height= 400)
gameplay_player_container.pack(fill = "x")

jugador = "X"

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
    for col in range(3):
        boton_col_0 = botones[col][0]
        boton_col_1 = botones[col][1]
        boton_col_2 = botones[col][2]

        if boton_row_0.num_assign == boton_row_1.num_assign and boton_row_1.num_assign == boton_row_2.num_assign:
            return boton_row_0.num_assign

        if boton_col_0.num_assign == boton_col_1.num_assign and boton_col_1.num_assign == boton_col_2.num_assign:
            return boton_col_0.num_assign

    return None


def jugar(row,col):
    print(f"{row}_{col}")

    global jugador
    boton = botones[row][col]
    if boton.cget("text")=="":
        boton.config(text = jugador)
        
        if jugador == "X":
            boton.num_assign = 1
            jugador = "O"
        else:
            boton.num_assign = 2
            jugador = "X"

        ganador = validar_juego()
        if ganador != None:
            if ganador == 1:
                test_congratulations_player.config(text="El jugador 1 (X) ha ganado")
            elif ganador == 2:
                test_congratulations_player.config(text="El jugador 2(O) ha ganado")
        else:
            test_congratulations_player(text="No hay ganadores")
        

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
'''
    if boton.button_id == "Cell (0, 0)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
            if boton.button_id == "" and boton.button_id == "Cell (0, 1)" and boton.button_id == "Cell (0, 2)":
                test_congratulations_player.config(text = "El jugador 1 (X), es el ganador")


    elif boton.button_id == "Cell (0, 1)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton.button_id == "Cell (0, 2)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton.button_id == "Cell (1, 0)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton.button_id == "Cell (1, 1)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton.button_id == "Cell (1, 2)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton.button_id == "Cell (2, 0)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton.button_id == "Cell (2, 1)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    elif boton.button_id == "Cell (2, 2)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"
'''

test_congratulations_player = tk.Label(congratulations_player_text_container, text = "Test")
test_congratulations_player.place(relx = 0.5, rely= 0.12, anchor="center")
test_congratulations_player.pack()

for row in range(3):
    for col in range(3):

        boton = tk.Button(gameplay_player_container,
            text = "",
            width=10,
            height=5,
            cursor = "cross",
            command = lambda r = row, c = col: jugar(r,c)
        )

        boton.num_assign = None
        #boton.config(command=lambda b=boton: marcar_celda(b))        
        boton.grid(row=row, column=col)
        botones[row][col] = boton

root.mainloop()