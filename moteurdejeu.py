import random
from tkinter import *

taille_de_la_grille = 9
nombre_de_bombes = 10
jeu_termine = False


def creer_grille():
    grille = [[0 for _ in range(taille_de_la_grille)] for _ in range(taille_de_la_grille)]

    bombes_placees = 0

    while bombes_placees < nombre_de_bombes:
        x = random.randint(0, taille_de_la_grille - 1)
        y = random.randint(0, taille_de_la_grille - 1)

        if grille[y][x] == 0:
            grille[y][x] = 1
            bombes_placees += 1

    return grille


def compter_bombes_autour(x, y):
    total = 0

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < taille_de_la_grille and 0 <= ny < taille_de_la_grille:
                if grille[ny][nx] == 1:
                    total += 1

    return total


def reveler_case(x, y):
    global jeu_termine

    if jeu_termine:
        return

    bouton = boutons[y][x]

    if bouton["state"] == "disabled":
        return

    if grille[y][x] == 1:
        bouton.config(text="💣", bg="red")
        jeu_termine = True
        print("GAME OVER")
        return

    nb = compter_bombes_autour(x, y)

    bouton.config(state="disabled", bg="lightgrey")

    if nb > 0:
        bouton.config(text=str(nb))
    else:
        bouton.config(text="0")


def creer_interface():
    for y in range(taille_de_la_grille):
        ligne = []

        for x in range(taille_de_la_grille):
            bouton = Button(
                fenetre,
                text="🟩",
                width=3,
                command=lambda x=x, y=y: reveler_case(x, y)
            )

            bouton.grid(row=y, column=x)
            ligne.append(bouton)

        boutons.append(ligne)


fenetre = Tk()
fenetre.title("Démineur (version simple)")

grille = creer_grille()
boutons = []

creer_interface()

fenetre.mainloop()