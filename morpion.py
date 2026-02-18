
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLayout, QHBoxLayout, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
class QuizView( QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion")
        self.resize(1920, 1080)
        self.setStyleSheet("background-color: darkred;")
        self.setMinimumSize(800, 600)
        self.question_label = QLabel("TIC TAC TOE GAME", self)
        self.question_label.setAlignment(Qt.AlignCenter) # Centre the text
        self.question_label.move(50, 50)
        # ----- Main layout -----
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.question_label)
      
        #------board_layout----
        board_layout = QGridLayout()
        for row in range(3):
            for col in range(3):
                button = QPushButton(f"Button {row},{col}")
                button.setFixedSize(200,200)
                board_layout.addWidget(button, row, col)
        board_layout.setHorizontalSpacing(10)

        
        main_layout.addLayout(board_layout)

        self.setLayout(main_layout)



