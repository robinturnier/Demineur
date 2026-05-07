import random
import tkinter as tk
from tkinter import *

taille_de_la_grille = 9
nombre_de_bombes = 10
nombre_de_drapeau = nombre_de_bombes
jeu_termine = False
mode_drapeau = False 

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
    for deplacement_y in [-1, 0, 1]:
        for deplacement_x in [-1, 0, 1]:
            nouveau_x = x + deplacement_x
            nouveau_y = y + deplacement_y
            if 0 <= nouveau_x < taille_de_la_grille and 0 <= nouveau_y < taille_de_la_grille:
                if grille[nouveau_y][nouveau_x] == 1:
                    total += 1
    return total

def reveler_case(x, y):
    global jeu_termine
    global nombre_de_drapeau 
    if jeu_termine:
        return
    bouton = boutons[y][x]
    if bouton["state"] == "disabled":
        return

    if mode_drapeau == False:
        if bouton["text"] == "🚩":   # on ne creuse pas sous un drapeau
            return
        if grille[y][x] == 1:
            bouton.config(text="💣", bg="red") #la bombe met fin a la partie
            jeu_termine = True
            print("GAME OVER")
            return
        nb = compter_bombes_autour(x, y)
        bouton.config(state="disabled", bg="lightgrey")
        bouton.config(text=str(nb) if nb > 0 else "0")
    else:
        if bouton["text"] == "🚩":   
            bouton.config(text="🟩")
            nombre_de_drapeau += 1
        else:
            if nombre_de_drapeau > 0:
                bouton.config(text="🚩")
                nombre_de_drapeau -= 1
                gagner()
            else:
                print('pas assez de drapeau')
                return

def mode__drapeau():#voir si on pose un drapeau ou si on creuse
    global mode_drapeau             
    if var.get() == 1:              
        mode_drapeau = True
    else:
        mode_drapeau = False

def creer_interface():
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

    boutton_drapeau = Checkbutton(     #créer un boutton pour activer/désactiver le mode drapeau
        frame_panel,
        text="drapeau",
        width=10,
        variable=var,
        onvalue=1,
        offvalue=0,
        command=mode__drapeau       #reférer a la fonction pour activer les changements liés au passage en mode drapeau/creusage
    )
    boutton_drapeau.pack()

def gagner():
    ok = 0
    for i in range(taille_de_la_grille):
        for j in range(taille_de_la_grille):
            if grille[i][j] == 0:
                ok += 1
            elif grille[i][j] == 1 and boutons[i][j]["text"] == "🚩":
                ok += 1
    print(ok)
    if ok == taille_de_la_grille**2 :
        print("Vous avez GAGNER")
        jeu_termine = True
        
            


fenetre = tk.Tk()
fenetre.title("Démineur")
var = tk.IntVar()                   


frame_grille = tk.Frame(fenetre, padx=10, pady=10)     #créer une partie de la page pour la grille
frame_panel  = tk.Frame(fenetre, padx=10, pady=10, bg="lightgrey", width=150)# l'autre partie pour les options
frame_grille.pack(side="left")
frame_panel.pack(side="right", fill="y")

grille = creer_grille()
boutons = []
creer_interface()
fenetre.mainloop()
