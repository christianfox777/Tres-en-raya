import tkinter as tk

root = tk.Tk()
root.title("Prueba de botones de x y o")

jugador = "X"

def marcar_celda(boton):
    global jugador

    if boton["text"] == "Cell (0, 0)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    elif boton["text"] == "Cell (0, 1)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton["text"] == "Cell (0, 2)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton["text"] == "Cell (1, 0)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton["text"] == "Cell (1, 1)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton["text"] == "Cell (1, 2)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton["text"] == "Cell (2, 0)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    
    elif boton["text"] == "Cell (2, 1)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    elif boton["text"] == "Cell (2, 2)":
        boton.config(text=jugador, fg = "#000000")

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

for row in range(3):
    for col in range(3):

        boton = tk.Button(root,
            text=f"Cell ({row}, {col})",
            width=10,
            height=5,
            fg = "#f0f0f0",
            bg = "#f0f0f0",
            activebackground= "#f0f0f0",
            activeforeground= "#f0f0f0"
        )

        boton.config(command=lambda b=boton: marcar_celda(b))
        boton.grid(row=row, column=col)


root.mainloop()