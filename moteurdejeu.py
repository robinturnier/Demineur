import random
from tkinter import *

# ----------------- PARAMÈTRES -----------------

taille_grille = 9
nombre_bombes = 10

jeu_termine = False

# ----------------- GRILLE -----------------

def generer_grille():
    grille = [[0 for _ in range(taille_grille)] for _ in range(taille_grille)]

    bombes_placees = 0

    while bombes_placees < nombre_bombes:
        x = random.randint(0, taille_grille - 1)
        y = random.randint(0, taille_grille - 1)

        if grille[y][x] == 0:
            grille[y][x] = 1
            bombes_placees += 1

    return grille


# ----------------- COMPTER BOMBES -----------------

def compter_bombes_autour(x, y):
    total = 0

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < taille_grille and 0 <= ny < taille_grille:
                if grille[ny][nx] == 1:
                    total += 1

    return total


# ----------------- FLOOD (OUVERTURE CASES VIDES) -----------------

def ouvrir_cases_vides(x, y):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < taille_grille and 0 <= ny < taille_grille:

                bouton = boutons[ny][nx]

                if bouton["state"] == "normal" and bouton["text"] != "🚩":

                    if grille[ny][nx] == 0:
                        nb = compter_bombes_autour(nx, ny)

                        bouton.config(state="disabled", bg="lightgrey")

                        if nb > 0:
                            bouton.config(text=str(nb))


# ----------------- REVELER CASE -----------------

def reveler_case(x, y):
    global jeu_termine

    if jeu_termine:
        return

    bouton = boutons[y][x]

    if bouton["state"] == "disabled" or bouton["text"] == "🚩":
        return

    # bombe
    if grille[y][x] == 1:
        bouton.config(text="💣", bg="red")
        jeu_termine = True
        print("💥 GAME OVER")
        return

    nb = compter_bombes_autour(x, y)

    bouton.config(state="disabled", bg="lightgrey")

    if nb > 0:
        bouton.config(text=str(nb))
    else:
        bouton.config(text="")
        ouvrir_cases_vides(x, y)


# ----------------- DRAPEAU -----------------

def poser_drapeau(event, x, y):
    if jeu_termine:
        return

    bouton = boutons[y][x]

    if bouton["state"] == "disabled":
        return

    if bouton["text"] == "🚩":
        bouton.config(text="🟩")
    else:
        bouton.config(text="🚩")


# ----------------- INTERFACE -----------------

def creer_grille_interface():
    for y in range(taille_grille):
        ligne_boutons = []

        for x in range(taille_grille):

            bouton = Button(
                fenetre,
                text="🟩",
                width=3,
                command=lambda x=x, y=y: reveler_case(x, y)
            )

            bouton.bind("<Button-3>", lambda e, x=x, y=y: poser_drapeau(e, x, y))

            bouton.grid(row=y, column=x)
            ligne_boutons.append(bouton)

        boutons.append(ligne_boutons)


# ----------------- LANCEMENT -----------------

fenetre = Tk()
fenetre.title("Démineur")

grille = generer_grille()
boutons = []

creer_grille_interface()

fenetre.mainloop()