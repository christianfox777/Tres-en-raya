import tkinter as tk

root = tk.Tk()
root.title("Prueba de botones de x y o")

congratulations_player_text_container = tk.Frame(root, width=400, height=200)
congratulations_player_text_container.pack(fill="x")
gameplay_player_container = tk.Frame(root, width=400, height= 400)
gameplay_player_container.pack(fill = "x")

jugador = "X"

def marcar_celda(boton):
    global jugador

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

test_congratulations_player = tk.Label(congratulations_player_text_container, text = "Test")
test_congratulations_player.place(relx = 0.5, rely= 0.12, anchor="center")
test_congratulations_player.pack()

for row in range(3):
    for col in range(3):

        boton = tk.Button(gameplay_player_container,
            text=f"Cell ({row}, {col})",
            width=10,
            height=5,
            fg = "#f0f0f0",
            bg = "#f0f0f0",
            activebackground= "#f0f0f0",
            activeforeground= "#f0f0f0",
            cursor = "cross"
        )

        boton.button_id = f"Cell ({row}, {col})"
        boton.config(command=lambda b=boton: marcar_celda(b))        
        boton.grid(row=row, column=col)


root.mainloop()