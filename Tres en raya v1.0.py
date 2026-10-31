#Tres en Raya v1.0 Christian Suarez, Nicolas Rivera y Christopher Barreno
#27.09.2026
import tkinter as tk
window_title = tk.Tk()
window_title.title("Tres en Raya v.1.0")
window_title.geometry("800x700")
window_title.configure(bg= "#CCE6F4")

def gameplay_tres_en_raya():
    for row in range(3):
        for colum in range(3):
            tk.Button(window_title,
                text=f"Cell ({row}, {colum})",
                width=10,
                height=5
            ).grid(row=row, column=colum)

#Ventana de inicio
titulo = tk.Label(window_title, text = "TRES EN RAYA", 
                  font=("Gill Sans Ultra Bold", 24), 
                  bg= "#CCE6F4", fg= "#175676")
titulo.pack()
titulo.place(relx = 0.5, rely= 0.12, anchor="center")
text1 = tk.Label(window_title, text = "Creado por:", font = ("Arial, 12"), 
                 bg= "#CCE6F4", fg= "#175676")
text1.pack()
text1.place(relx = 0.5, rely= 0.18, anchor="center")
text2 = tk.Label(window_title, text = "Christian Suarez, Nicolas Rivera y Christopher Barreno", 
                 font = ("Arial, 12"),
                 bg= "#CCE6F4", fg="#175676")
text2.pack()
text2.place(relx= 0.5, rely= 0.228,anchor="center")

#Player Selection



#Matriz del juego

def gameplay_tres_en_raya():
    for row in range(3):
        for colum in range(3):
            tk.Button(window_title,
                text=f"Cell ({row}, {colum})",
                width=10,
                height=5
            ).grid(row=row, column=colum)

Begin_button = tk.Button(window_title,
                         command=gameplay_tres_en_raya, 
                         text = "EMPEZAR", 
                         font = ("Gill Sans Ultra Bold", 20),
                         bg = "#BA324F",
                         fg= "#F3F2F2")
Begin_button.pack()
Begin_button.place(relx=0.5 , rely= 0.8, anchor="center")

window_title.mainloop()




