# 🧨 Projet NSI – Jeu de Démineur en Python

## 📌 Description
Ce projet a été réalisé dans le cadre de la spécialité NSI en classe de Première.  
Il consiste à développer un jeu inspiré du démineur, en réutilisant plusieurs notions vues en cours comme les matrices, les structures de données et la gestion de fichiers.

---

## 🎮 Fonctionnement du jeu

- Une grille carrée (x × x) est générée aléatoirement selon la difficulté choisie  
- Des bombes sont cachées dans certaines cases  
- Le joueur dispose d’un nombre limité de drapeaux pour marquer les cases suspectes  

### 🔍 Actions possibles
- Cliquer sur une case pour la révéler  
- Placer un drapeau pour signaler une bombe potentielle  

### 📊 Indications
Lorsqu’une case est révélée :
- Un nombre s’affiche indiquant le nombre de bombes dans les cases voisines  
- Le calcul se fait sur une zone de 3×3 autour de la case  

### 🏁 Conditions de fin
- Victoire : toutes les bombes sont correctement identifiées  
- Défaite : une bombe est déclenchée  

---

## ⚙️ Moteur du jeu

- Langage : Python  
- Interface graphique : tkinter  

### Fonctionnalités principales
- Génération aléatoire des cartes  
- Gestion des interactions utilisateur  
- Utilisation de matrices pour représenter la grille  
- Calcul des cases voisines  

---

## 💾 Stockage des données

Les données des parties sont enregistrées dans un fichier CSV.

### Données stockées
- Nombre de bombes  
- Nombre de drapeaux utilisés  
- Nombre de drapeaux disponibles  
- Taille de la carte  
- Position des bombes  

---

## 🧠 Notions de NSI utilisées

- Listes et matrices  
- Dictionnaires  
- Lecture et écriture de fichiers CSV  
- Algorithmes de parcours  
- Interface graphique  

---

