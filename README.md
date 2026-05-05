# 🧨 Projet NSI – Jeu de Démineur en Python

## 📌 Description
Ce projet a été réalisé dans le cadre de la spécialité NSI en classe de Première.  
Il s’agit d’une version simplifiée du jeu du démineur développée en Python avec une interface graphique.

L’objectif est de réinvestir les notions de programmation vues en cours à travers un projet concret et interactif.

---

## 🎮 Fonctionnement du jeu

- Une grille carrée (9 × 9) est générée aléatoirement
- 10 bombes sont placées de manière aléatoire sur la grille
- Le joueur clique sur les cases pour les révéler

### 🔍 Principe du jeu
- Si la case contient une bombe 💣 → la partie est perdue
- Sinon, un nombre s’affiche indiquant le nombre de bombes présentes dans les cases voisines

Le calcul est effectué sur une zone de 3×3 autour de la case cliquée.

---

## ⚙️ Moteur du jeu

- Langage : Python
- Bibliothèque graphique : tkinter
- Génération aléatoire : module `random`

### Fonctionnalités principales
- Création dynamique d’une grille de boutons
- Placement aléatoire des bombes
- Gestion des clics utilisateur
- Calcul des bombes adjacentes
- Fin de partie en cas de bombe déclenchée

---

## 🧠 Structures de données utilisées

- **Matrices (listes 2D)** :
  - `grille` → stocke les bombes (0 ou 1)
  - `boutons` → stocke les boutons de l’interface

Chaque position `[y][x]` correspond à une case du jeu.

---

## 🖥️ Interface graphique

L’interface est construite avec `tkinter` :
- Chaque case est un bouton
- Un clic déclenche la révélation de la case
- Les cases révélées changent de couleur et affichent une valeur

---

## 📁 Organisation du projet

📁 Projet
├── main.py   # Code principal du jeu

---

## 🧠 Notions de NSI utilisées

- Listes et listes 2D (matrices)
- Conditions et boucles imbriquées
- Algorithmes de parcours de grille
- Gestion d’événements (clics souris)
- Interface graphique avec tkinter
- Utilisation de fonctions et variables globales

---

## 🚀 Améliorations possibles

- Ajout de drapeaux 🚩
- Révélation automatique des zones vides
- Compteur de temps
- Système de victoire
- Choix de difficulté (taille + bombes)
