import random
from tkinter import *

def generer_grille(difficulte):
    if difficulte == 1:
        taille_grille = 9
        nombre_de_bombe = 10
        nombre_de_drapeau = 10
    elif difficulte == 2:
        taille_grille = 16
        nombre_de_bombe = 40
        nombre_de_drapeau = 40
    elif difficulte == 3:
        taille_grille = 20
        nombre_de_bombe = 85
        nombre_de_drapeau = 85

    grille = [[0 for _ in range(taille_grille)] for _ in range(taille_grille)]

    nombre_de_bombe_place = 0
    while nombre_de_bombe_place < nombre_de_bombe:
        x = random.randint(0, taille_grille - 1)
        y = random.randint(0, taille_grille - 1)

        if grille[y][x] != 1:
            grille[y][x] = 1
            nombre_de_bombe_place += 1

    return grille, taille_grille, nombre_de_drapeau


def poser_drapeau():
    global nombre_de_drapeau
    if nombre_de_drapeau > 0:
        nombre_de_drapeau -= 1
        label_drapeau.config(text=nombre_de_drapeau)


def afficher_grille(fenetre, grille, taille_grille):
    global label_drapeau

    label_drapeau = Label(fenetre, text=nombre_de_drapeau)
    label_drapeau.grid(row=0, column=0, columnspan=taille_grille)

    for y, ligne in enumerate(grille):
        for x, case in enumerate(ligne):
            bouton = Button(
                fenetre,
                text="🟩",
                width=3,
                relief="raised",
                command=poser_drapeau
            )
            bouton.grid(row=y+1, column=x)


def initialisation():
    global nombre_de_drapeau

    fenetre = Tk()
    fenetre.title("Démineur")

    grille, taille_grille, nombre_de_drapeau = generer_grille(1)

    afficher_grille(fenetre, grille, taille_grille)

    fenetre.mainloop()


initialisation()