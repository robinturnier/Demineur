import random
from tkinter import *

taille_de_la_grille = 9
nombre_de_bombes = 10
jeu_termine = False


def creer_grille():
    # création d'une matrice 2D remplie de 0 (pas de bombes)
    # chaque ligne est une nouvelle liste (important sinon bug de copie)
    grille = [[0 for _ in range(taille_de_la_grille)] for _ in range(taille_de_la_grille)]

    bombes_placees = 0

    while bombes_placees < nombre_de_bombes:
        # coordonnées aléatoires dans la grille
        x = random.randint(0, taille_de_la_grille - 1)
        y = random.randint(0, taille_de_la_grille - 1)

        # on vérifie qu'on ne met pas 2 bombes au même endroit
        if grille[y][x] == 0:
            grille[y][x] = 1
            bombes_placees += 1

    return grille


def compter_bombes_autour(x, y):
    total = 0

    # parcours des 8 cases autour + la case elle-même
    for deplacement_y in [-1, 0, 1]:
        for deplacement_x in [-1, 0, 1]:

            nouveau_x = x + deplacement_x
            nouveau_y = y + deplacement_y

            # évite de sortir de la grille (sinon crash index)
            if 0 <= nouveau_x < taille_de_la_grille and 0 <= nouveau_y < taille_de_la_grille:

                # grille[y][x] → y = ligne, x = colonne
                if grille[nouveau_y][nouveau_x] == 1:
                    total += 1

    return total


def reveler_case(x, y):
    global jeu_termine  # on modifie la variable globale

    if jeu_termine:
        return

    bouton = boutons[y][x]  # récupère le bouton correspondant à la case

    # évite de recliquer sur une case déjà révélée
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

                # lambda x=x, y=y  sinon toutes les cases auraient les meme co
                command=lambda x=x, y=y: reveler_case(x, y)
            )

            bouton.grid(row=y, column=x)
            ligne.append(bouton)
        boutons.append(ligne)


fenetre = Tk()
fenetre.title("Démineur")

grille = creer_grille()
boutons = []

creer_interface()

fenetre.mainloop()