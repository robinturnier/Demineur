import random
import tkinter as tk
from tkinter import *

taille_de_la_grille = 9
nombre_de_bombes = 10
nombre_de_drapeau = nombre_de_bombes
jeu_termine = False
mode_drapeau = False 

def creer_grille():
    """
    Fonction cree grille : cree une matrice de taille_de_la_grille² ( autant de colonne que de ligne)
    ensuite on genere un nombre aleatoire entre taille de la grille-1 pour ne pas depasser et 0 pour tt prend en compte
    => On fait ca pour x et y et ca donne des coordonée aleatoire
    OUT : grille
    """
    grille = []
    for i in range(taille_de_la_grille):
        ligne = []
        for j in range(taille_de_la_grille):
            ligne.append(0)
        grille.append(ligne)

    bombes = 0
    while bombes < nombre_de_bombes:
        x = random.randint(0, taille_de_la_grille - 1)
        y = random.randint(0, taille_de_la_grille - 1)
        if grille[y][x] == 0:
            grille[y][x] = 1
            bombes += 1

    return grille

def compter_bombes_autour(x, y):
    """
    IN: coordonée de la case cliquer
    dx,dy = deplacement a faire: -1 pour 1 en dessou / 1 a gauche ,1 pour 1 au dessu et 1 a droite et 0 pour aussi faire au dessu et en dessou du central
    nx ,ny = nouveau xy  a verifier si la valeur est 0
    => On verifie encore une fois qu'on ne sors pas de la grille
    OUT : nombre de bombe autour de la case
    """
    total = 0
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < taille_de_la_grille and 0 <= ny < taille_de_la_grille:
                if grille[ny][nx] == 1:
                    total += 1
    return total

def reveler_case(x, y):
    """
    IN : coordonée a reveler
    Révèle une case du démineur.

    - Si la case contient une bombe → fin de partie.
    - Sinon, affiche le nombre de bombes autour.
    - Si aucune bombe autour → révèle automatiquement les cases voisines (cascade) afin de ne pas a avoir a tout cliqué ( pour ressemble au jeu original)
    - Ignore les cases déjà révélées ou marquées avec un drapeau.
    """
    global jeu_termine, nombre_de_drapeau

    if jeu_termine:
        return

    bouton = boutons[y][x]

    if bouton["state"] == "disabled":
        return

    if bouton["text"] == "🚩":
        return

    if not mode_drapeau:

        if grille[y][x] == 1:
            bouton.config(text="💣", bg="red")
            jeu_termine = True

            for i in range(taille_de_la_grille):
                for j in range(taille_de_la_grille):
                    if grille[i][j] == 1:
                        boutons[i][j].config(text="💣")

            print("perdu")
            return

        nb = compter_bombes_autour(x, y)
        bouton.config(state="disabled", bg="lightgrey")

        if nb > 0:
            bouton.config(text=str(nb))
            if nb == 1:
                bouton.config(fg="blue")
            elif nb == 2:
                bouton.config(fg="green")
            elif nb == 3:
                bouton.config(fg="red")
        else:
            bouton.config(text="")

            # cascade simple
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < taille_de_la_grille and 0 <= ny < taille_de_la_grille:
                        if boutons[ny][nx]["state"] != "disabled":
                            reveler_case(nx, ny)

    else:
        if bouton["text"] == "🚩":
            bouton.config(text="🟩")
            nombre_de_drapeau += 1
        else:
            if nombre_de_drapeau > 0:
                bouton.config(text="🚩")
                nombre_de_drapeau -= 1
                gagner()

def mode__drapeau():
    """
    Manière d'eviter la gestion de clic gauche / clic droit lors de la pause de drapeau, il s'agit d'un on off qui modifie la case pour y rajouter un drapeau dessu
    => Les drapeaux servent a gagner donc obligatoire
    """
    global mode_drapeau
    if var.get() == 1:
        mode_drapeau = True
    else:
        mode_drapeau = False

def creer_interface():
    """
Fonction simple generant l'UI du jeu avec qlq couleur , les label et surtout la grille
    """
    for y in range(taille_de_la_grille):
        ligne = []
        for x in range(taille_de_la_grille):
            bouton = tk.Button(
                frame_grille,
                text="🟩",
                width=3,
                command=lambda x=x, y=y: reveler_case(x, y)
            )
            bouton.grid(row=y, column=x)
            ligne.append(bouton)
        boutons.append(ligne)

    Checkbutton(
        frame_panel,
        text="drapeau",
        variable=var,
        command=mode__drapeau
    ).pack()

def gagner():
    """
    Detection de victoire de la partie si toutes les cases avec bombes sont marqué d'un drapeau
    """
    global jeu_termine
    ok = 0
    for i in range(taille_de_la_grille):
        for j in range(taille_de_la_grille):
            if grille[i][j] == 0 and boutons[i][j]["state"] == "disabled":
                ok += 1
            if grille[i][j] == 1 and boutons[i][j]["text"] == "🚩":
                ok += 1

    if ok == taille_de_la_grille * taille_de_la_grille:
        print("gagné")
        jeu_termine = True

# Lignes permettant la mise en place et le demarrage du jeu
fenetre = tk.Tk()
fenetre.title("Demineur")

var = tk.IntVar()

frame_grille = Frame(fenetre)
frame_panel = Frame(fenetre)

frame_grille.pack(side="left")
frame_panel.pack(side="right")

grille = creer_grille()
boutons = []

creer_interface()

fenetre.mainloop()

