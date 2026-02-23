
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLayout, QHBoxLayout, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
class QuizView( QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion")  #Titre de la fenetre
        self.setFixedSize(1000, 1400) #Taille de la fenetre
        self.setStyleSheet("background-color: darkgreen;") #Couleur de l'arriere plan
        self.current_player = 'O'  # Commencer avec O

        self.question_label = QLabel("TIC TAC TOE GAME", self)  #Titre du jeu en haut
        self.question_label.setAlignment(Qt.AlignCenter) # Centre the text
        # ----- Main layout -----
        main_layout = QVBoxLayout()  #Création de l'environnement global
        main_layout.addWidget(self.question_label) #Rajoute le label du titre
      
        #------board_layout----
        board_layout = QGridLayout() #Crée la grille du morpion
        self.buttons = []  #Crée une liste pour stocker les boutons cliqué
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QPushButton("") #Crée bouton
                button.setFixedSize(200,200) #Taille des boutons
                button.setStyleSheet("background-color: lightgreen; font-size: 48px;") #Couleur des boutons
                button.clicked.connect(lambda checked, r=row, c=col: self.button_clicked(r, c)) #Connecte a la fonction des boutons cliqué les coordonées du bouton cliqué 
                board_layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)
        

        main_layout.addLayout(board_layout) #Rajoute la grid au layout

        self.setLayout(main_layout) #Met le main layout

    def button_clicked(self, row, col): #fonction pour detecter le clic d'un bouton
        button = self.buttons[row][col] #Coordonée du bouton cliqué
        button.setText(self.current_player)  # Mettre le symbole du joueur actuel
        button.setEnabled(False)  # Désactiver le bouton après le clic
        print(f"Le bouton a été cliqué ici {row},{col} - Joueur: {self.current_player}")
        self.current_player = 'X' if self.current_player == 'O' else 'O' #alterne entre rond et croix 






        



