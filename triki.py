import tkinter as tk
from tkinter import messagebox

# Variables del juego
player = "X"
game_over = False

# Función para verificar si hay un ganador
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def button_click(row, col):
    global player, game_over
    if buttons[row][col]["text"] == "" and not game_over:
        buttons[row][col]["text"] = player
        buttons[row][col]["bg"] = "#37474F" if player == "X" else "#455A64"
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"¡Jugador {player} gana!")
            game_over = True
        elif all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Tic Tac Toe", "¡Es un empate!")
            game_over = True
        else:
            player = "O" if player == "X" else "X"

def reset_game():
    global player, game_over
    player = "X"
    game_over = False
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["bg"] = "SystemButtonFace"

# Crear la ventana principal
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="#263238")

# Crear los botones
buttons = [[tk.Button(root, text="", font=('normal', 20), width=5, height=2, command=lambda r=i, c=j: button_click(r, c)) 
            for j in range(3)] for i in range(3)]

# Colocar los botones en la ventana
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text="Reiniciar", font="normal 15 bold", command=reset_game, bg="#546E7A", fg="white")
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Iniciar el bucle principal
root.mainloop()