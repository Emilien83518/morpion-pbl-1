import math

# Constantes pour les scores selon le sujet [cite: 29]
IA_GAGNE = 1000
JOUEUR_GAGNE = -1000
EGALITE = 0

class MorpionIA:
    def __init__(self):
        # Le plateau est une liste de 9 cases vides
        self.plateau = [" " for _ in range(9)]
        
    def afficher_plateau(self):
        """Affiche le plateau de jeu de manière lisible."""
        for i in range(0, 9, 3):
            print(f" {self.plateau[i]} | {self.plateau[i+1]} | {self.plateau[i+2]} ")
            if i < 6: print("-----------")

    def verifier_victoire(self, symbole):
        """Vérifie si le symbole (X ou O) a gagné[cite: 68]."""
        victoires = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(all(self.plateau[i] == symbole for i in combo) for combo in victoires)

    def evaluer_plateau(self):
        """Attribue un score à l'état actuel[cite: 66, 67]."""
        if self.verifier_victoire("O"): return IA_GAGNE
        if self.verifier_victoire("X"): return JOUEUR_GAGNE
        return EGALITE

    def coups_possibles(self):
        """Retourne la liste des index vides[cite: 130]."""
        return [i for i, x in enumerate(self.plateau) if x == " "]

    def minimax(self, profondeur, est_max):
        """
        L'algorithme récursif qui explore l'arbre des possibilités[cite: 46].
        profondeur: nombre de coups restants à explorer[cite: 61].
        est_max: True si c'est au tour de l'IA (Max), False pour l'humain (Min).
        """
        score = self.evaluer_plateau()

        # Conditions d'arrêt : victoire, défaite ou plus de place [cite: 28, 45]
        if score == IA_GAGNE or score == JOUEUR_GAGNE:
            return score
        if not self.coups_possibles() or profondeur == 0:
            return EGALITE

        if est_max:
            # Tour de l'IA : on veut le score le plus haut possible [cite: 47]
            meilleur_score = -math.inf
            for coup in self.coups_possibles():
                self.plateau[coup] = "O"
                score = self.minimax(profondeur - 1, False)
                self.plateau[coup] = " " # Backtracking
                meilleur_score = max(score, meilleur_score)
            return meilleur_score
        else:
            # Tour de l'humain : l'IA suppose qu'il jouera le mieux (score min) [cite: 48]
            meilleur_score = math.inf
            for coup in self.coups_possibles():
                self.plateau[coup] = "X"
                score = self.minimax(profondeur - 1, True)
                self.plateau[coup] = " " # Backtracking
                meilleur_score = min(score, meilleur_score)
            return meilleur_score

    def meilleur_coup(self, difficulte):
        """Calcule et affiche le meilleur coup pour l'IA[cite: 49, 52]."""
        meilleur_val = -math.inf
        coup_choisi = -1
        
        print("\n--- Analyse de l'IA ---")
        for coup in self.coups_possibles():
            self.plateau[coup] = "O"
            # La difficulté définit la profondeur de recherche [cite: 61]
            valeur_coup = self.minimax(difficulte, False)
            self.plateau[coup] = " "
            
            print(f"Coup {coup} : Score = {valeur_coup}") # Consigne: afficher les scores [cite: 52]
            
            if valeur_coup > meilleur_val:
                meilleur_val = valeur_coup
                coup_choisi = coup
        
        return coup_choisi

# --- Lancement du jeu ---
jeu = MorpionIA()
# Niveau de difficulté (profondeur de recherche) [cite: 52, 60]
# 1 = Facile, 9 = Imbattable
difficulte = 9 

print("Bienvenue au Morpion IA !")
while jeu.coups_possibles() and not (jeu.verifier_victoire("X") or jeu.verifier_victoire("O")):
    jeu.afficher_plateau()
    
    # Tour de l'humain
    choix = int(input("\nVotre coup (0-8) : "))
    if jeu.plateau[choix] == " ":
        jeu.plateau[choix] = "X"
        
        # Tour de l'IA
        if jeu.coups_possibles() and not jeu.verifier_victoire("X"):
            print("\nL'IA réfléchit...")
            ia_coup = jeu.meilleur_coup(difficulte)
            jeu.plateau[ia_coup] = "O"
    else:
        print("Case déjà prise !")

jeu.afficher_plateau()
print("\nFin de la partie !")