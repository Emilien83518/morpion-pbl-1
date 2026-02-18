import sys
from PyQt5.QtGui import QIcon
# Main class for the PyQt5 application
from PyQt5.QtWidgets import QApplication
# Import the main application window
from view.quiz_view import QuizView
app = QApplication(sys.argv) # Creates the application
app.setWindowIcon(QIcon("resources/quizicon.png"))
window = QuizView() # Creates the window
window.show() # Displays the window
sys.exit(app.exec_()) # Starts the application loop and exits cleanly
