# 🧨 Projet NSI – Jeu de Démineur en Python

## 📌 Description
Ce projet a été réalisé dans le cadre de la spécialité NSI en classe de Première.  
Il s’agit d’une version fonctionnelle du jeu du démineur développée en Python avec une interface graphique.

Le but est de reproduire les mécaniques principales du jeu tout en appliquant les notions vues en cours.

---

## 🎮 Fonctionnement du jeu

- Une grille carrée (9 × 9) est générée aléatoirement
- 10 bombes sont placées sur la grille
- Le joueur interagit avec les cases via des boutons

---

## 🔍 Principe du jeu

- 💣 Bombe → défaite immédiate
- 🔢 Nombre → indique le nombre de bombes autour
- ⬜ Case vide → déclenche une cascade automatique

### 💡 Détails importants
- Le calcul des bombes se fait sur les 8 cases autour (zone 3×3)
- Les cases vides révèlent automatiquement leurs voisines
- Les cases déjà révélées ne peuvent pas être recliquées

---

## 🚩 Système de drapeaux

Un mode "drapeau" est disponible :

- Activation via une case à cocher
- Permet de poser/enlever un drapeau 🚩
- Nombre de drapeaux limité au nombre de bombes
- Indispensable pour gagner

---

## 🏆 Condition de victoire

Le joueur gagne si :

- Toutes les cases sans bombe sont révélées  
ET  
- Toutes les bombes sont correctement marquées avec un drapeau 🚩

---

## ⚙️ Moteur du jeu

- Langage : Python  
- Interface graphique : tkinter  
- Génération aléatoire : module `random`

---

## ⚡ Fonctionnalités implémentées

- Génération dynamique de la grille
- Placement aléatoire des bombes
- Révélation des cases
- Affichage du nombre de bombes adjacentes
- Cascade automatique des zones vides
- Mode drapeau activable
- Gestion du nombre de drapeaux
- Détection de victoire
- Détection de défaite + affichage des bombes

---

## 🧠 Structures de données

- Liste 2D (`grille`)  
  → contient les bombes (0 = vide, 1 = bombe)

- Liste 2D (`boutons`)  
  → contient les boutons tkinter

Chaque case est accessible via `[y][x]`.

---

## 🖥️ Interface graphique

- Chaque case est un bouton 🟩
- Couleurs dynamiques :
  - Bleu → 1
  - Vert → 2
  - Rouge → 3
- Bombe affichée en 💣
- Drapeau affiché en 🚩

---

## 📁 Organisation du projet

📁 Projet  
├── main.py   # Code principal du jeu  

---

## 🧠 Notions de NSI utilisées

- Listes et matrices (2D)
- Parcours de grille
- Conditions / boucles imbriquées
- Gestion d’événements (clics)
- Interface graphique avec tkinter
- Fonctions et variables globales

---

