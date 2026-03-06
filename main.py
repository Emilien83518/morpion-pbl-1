import sys
import random
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, 
                             QPushButton, QMessageBox, QApplication, QComboBox, QHBoxLayout)
from PyQt5.QtCore import Qt

class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IMPOSSIBLE TIC TAC TOE GAME")
        self.setFixedSize(600, 850)
        self.setStyleSheet("background-color: #3c667d;") 

        # This is the current state of the game
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.loss_streak = 0
        self.score_x = 0
        self.score_o = 0
        self.game_mode = "Player vs AI"
        self.difficulty = "Hard"

        # Menu
        self.menu_layout = QVBoxLayout()
        
        # Game mode
        mode_hbox = QHBoxLayout()
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Player vs AI", "Player vs Player"])
        self.mode_selector.currentTextChanged.connect(self.change_mode)
        mode_hbox.addWidget(QLabel("<font color='white'>Mode:</font>"))
        mode_hbox.addWidget(self.mode_selector)
        
        # Ai difficulty
        self.diff_hbox = QHBoxLayout()
        self.diff_selector = QComboBox()
        self.diff_selector.addItems(["Hard", "Easy"])
        self.diff_selector.currentTextChanged.connect(self.change_difficulty)
        self.diff_label = QLabel("<font color='white'>Difficulty:</font>")
        self.diff_hbox.addWidget(self.diff_label)
        self.diff_hbox.addWidget(self.diff_selector)

        # Score for 1v1
        self.score_widget = QWidget()
        self.score_layout = QHBoxLayout(self.score_widget)
        self.score_label_x = QLabel(f"player X: {self.score_x}")
        self.score_label_o = QLabel(f"player O: {self.score_o}")
        score_style = "color: #ecf0f1; font-size: 18px; font-weight: bold; background: #2980b9; "
        self.score_label_x.setStyleSheet(score_style)
        self.score_label_o.setStyleSheet(score_style)
        self.score_layout.addWidget(self.score_label_x)
        self.score_layout.addWidget(self.score_label_o)
        self.score_widget.setVisible(False)

        combo_style = """
            QComboBox { 
                background-color: #34495e; color: white; padding: 5px; 
                font-size: 16px; border-radius: 5px; min-width: 150px;
            }
        """
        self.mode_selector.setStyleSheet(combo_style)
        self.diff_selector.setStyleSheet(combo_style)

        self.menu_layout.addLayout(mode_hbox)
        self.menu_layout.addLayout(self.diff_hbox)
        self.menu_layout.addWidget(self.score_widget)

        # Status and loss streak
        self.status_label = QLabel("YOU PLAY -> X", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold; margin: 10px;")

        self.streak_label = QLabel("Streak Loss vs AI: 0", self)
        self.streak_label.setAlignment(Qt.AlignCenter)
        self.streak_label.setStyleSheet("color: #e74c3c; font-size: 18px; font-weight: bold; margin-bottom: 10px;")

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.menu_layout)
        main_layout.addWidget(self.status_label)

        board_layout = QGridLayout()
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(150, 150)
                button.setStyleSheet("QPushButton { background-color: #34495e; color: white; font-size: 60px; }")
                button.clicked.connect(lambda chk, r=row, c=col: self.handle_click(r, c))
                board_layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)

        main_layout.addLayout(board_layout)
        main_layout.addWidget(self.streak_label)
        self.setLayout(main_layout)

    def change_mode(self, mode):
        self.game_mode = mode
        is_ai = mode == "Player vs AI"
        
        #controls what is shown or hidden
        self.diff_selector.setVisible(is_ai)
        self.diff_label.setVisible(is_ai)
        self.streak_label.setVisible(is_ai)
        self.score_widget.setVisible(not is_ai)
        
        # Resets score if player decides to change mode
        self.score_x = 0
        self.score_o = 0
        self.update_score_labels()
        
        self.reset_game()

    def change_difficulty(self, diff):
        self.difficulty = diff
        self.reset_game()

    def update_score_labels(self):
        self.score_label_x.setText(f"Player X: {self.score_x}")
        self.score_label_o.setText(f"Player O: {self.score_o}")

    def handle_click(self, r, c):
        if self.board[r][c] == "":
            if self.game_mode == "Player vs AI":
                if self.make_move(r, c, "X"): return 
                self.status_label.repaint() 
                self.ai_move()
            else:
                current = self.current_player
                if self.make_move(r, c, current): return
                self.current_player = "O" if current == "X" else "X"
                self.status_label.setText(f"YOU PLAY -> {self.current_player}")

    def ai_move(self):
        move = None
        if self.difficulty == "Easy":
            available = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
            if available: move = random.choice(available)
        else:
            best_val = -float('inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == "":
                        self.board[r][c] = "O"
                        score = self.minimax(self.board, False)
                        self.board[r][c] = ""
                        if score > best_val:
                            best_val = score
                            move = (r, c)
        if move: self.make_move(move[0], move[1], "O")

    def minimax(self, state, is_maximizing):
        if self.Terminal(state, "O"): return 10
        if self.Terminal(state, "X"): return -10
        if not any("" in row for row in state): return 0
        if is_maximizing:
            best = -float('inf')
            for r in range(3):
                for c in range(3):
                    if state[r][c] == "":
                        state[r][c] = "O"
                        best = max(best, self.minimax(state, False))
                        state[r][c] = ""
            return best
        else:
            best = float('inf')
            for r in range(3):
                for c in range(3):
                    if state[r][c] == "":
                        state[r][c] = "X"
                        best = min(best, self.minimax(state, True))
                        state[r][c] = ""
            return best

    def make_move(self, row, col, player):
        self.board[row][col] = player
        self.buttons[row][col].setText(player)
        self.buttons[row][col].setEnabled(False)
        color = "#e74c3c" if player == "X" else "#f1c40f"
        self.buttons[row][col].setStyleSheet(f"background-color: #34495e; color: {color}; font-size: 60px; ")

        if self.check_winner(player):
            if self.game_mode == "Player vs AI":
                if player == "O": self.loss_streak += 1
                else: self.loss_streak = 0
                self.streak_label.setText(f"Loss Streak vs AI: {self.loss_streak}")
            else:
                if player == "X": self.score_x += 1
                else: self.score_o += 1
                self.update_score_labels()
            
            self.end_game(f"Player {player} wins !")
            return True

        if self.is_draw():
            self.end_game("Draw !")
            return True
        return False

    def Terminal(self, b, p):
        wins = [[b[0][0], b[0][1], b[0][2]], [b[1][0], b[1][1], b[1][2]], [b[2][0], b[2][1], b[2][2]],
                [b[0][0], b[1][0], b[2][0]], [b[0][1], b[1][1], b[2][1]], [b[0][2], b[1][2], b[2][2]],
                [b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]]
        return [p, p, p] in wins

    def check_winner(self, p): return self.Terminal(self.board, p)
    def is_draw(self): return not any("" in row for row in self.board)

    def end_game(self, message):
        QMessageBox.information(self, "Game Over", message)
        self.reset_game()

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in self.buttons:
            for btn in row:
                btn.setText("")
                btn.setEnabled(True)
                btn.setStyleSheet("background-color: #34495e; color: white; font-size: 60px; ")
        self.status_label.setText("YOU PLAY -> X" if self.game_mode == "Player vs AI" else "YOU PLAY -> X")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizView()
    window.show()
    sys.exit(app.exec_())