
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLayout, QHBoxLayout, QRadioButton, QPushButton
from PyQt5.QtCore import Qt
class QuizView( QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightblue;")
        self.setMinimumSize(800, 600)
        self.question_label = QLabel("What is the capital of France?", self)
        #self.question_label.setAlignment(Qt.AlignCenter) # Centre the text
        self.question_label.move(50, 100)
        # ----- Main layout -----
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.question_label)
        #---- answer layout-----
        answer_layout = QVBoxLayout()
        answer_1= QRadioButton("Paris")
        answer_2= QRadioButton('Lyon')
        answer_3= QRadioButton('Marseille')
        answer_4= QRadioButton('Bordeaux')
        answer_layout.addWidget(answer_1)
        answer_layout.addWidget(answer_2)
        answer_layout.addWidget(answer_3)
        answer_layout.addWidget(answer_4)
        #------nav_layout----
        nav_layout = QHBoxLayout()
        nav_prev=QPushButton("previous")
        nav_next=QPushButton('next')
        nav_layout.addWidget(nav_prev)
        nav_layout.addWidget(nav_next)


        main_layout.addLayout(answer_layout)
        main_layout.addLayout(nav_layout)

        self.setLayout(main_layout)



