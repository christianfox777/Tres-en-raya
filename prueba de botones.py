import tkinter as tk

root = tk.Tk()
root.title("Prueba de botones de x y o")

jugador = "X"

def marcar_celda(boton):
    global jugador

    if boton["text"] == "":
        boton.config(text=jugador)

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"


for row in range(3):
    for col in range(3):

        boton = tk.Button(
            root,
            text="",
            width=10,
            height=5
        )

        boton.config(command=lambda b=boton: marcar_celda(b))
        boton.grid(row=row, column=col)


root.mainloop()