#AI
#max player: wants to maximise score
#min player: wants to minimise score
#def terminal: terminal state means the game is over
#def value: value of terminal state
#def player: determines whose turn it is in any given game state (either max or min)
#def action: gives all the possible actions we can take in that state  
#def results: tells what the new state of the game will be after the action 

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt


class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion")
        self.setFixedSize(600, 700)
        self.setStyleSheet("background-color: lightblue;")

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.pvp_mode = False

        # NEW: stats (AI vs Player only)
        self.losses = 0
        self.draws = 0

        # UI Elements
        self.status_label = QLabel("YOUR TURN (X)", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet(
            "color: white; font-size: 24px; font-weight: bold; margin: 10px;"
        )

        self.mode_button = QPushButton("Switch to Player vs Player")
        self.mode_button.clicked.connect(self.toggle_mode)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.mode_button)

        board_layout = QGridLayout()
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(150, 150)
                button.setStyleSheet("""
                    QPushButton {
                        background-color: lightgreen;
                        color: white;
                        font-size: 60px;
                        border-radius: 10px;
                    }
                    QPushButton:hover {
                        background-color: #4e6a85;
                    }
                """)
                button.clicked.connect(lambda chk, r=row, c=col: self.handle_click(r, c))
                board_layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)

        main_layout.addLayout(board_layout)

        # NEW: bottom-left stats
        self.stats_label = QLabel("Losses: 0 | Draws: 0")
        self.stats_label.setAlignment(Qt.AlignLeft)
        self.stats_label.setStyleSheet("color: white; font-size: 16px; margin: 10px;")

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.stats_label)
        bottom_layout.addStretch()

        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)

    def toggle_mode(self):
        self.pvp_mode = not self.pvp_mode
        self.mode_button.setText(
            "Switch to Player vs AI" if self.pvp_mode else "Switch to Player vs Player"
        )
        self.reset_game()
        self.status_label.setText(
            "Player vs Player — Player X starts" if self.pvp_mode else "YOUR TURN (X)"
        )

    def handle_click(self, r, c):
        if self.board[r][c] != "":
            return

        if self.make_move(r, c, self.current_player):
            return

        if self.pvp_mode:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.setText(f"PLAYER {self.current_player}'S TURN")
        else:
            self.status_label.repaint()
            self.ai_move()
            self.current_player = "X"

    def make_move(self, row, col, player):
        self.board[row][col] = player
        self.buttons[row][col].setText(player)
        self.buttons[row][col].setEnabled(False)

        color = "#e74c3c" if player == "X" else "#FF6B9A"
        self.buttons[row][col].setStyleSheet(
            f"background-color: #34495e; color: {color}; font-size: 60px; border-radius: 10px;"
        )

        if self.check_winner(player):
            self.handle_game_end(player)
            return True

        if self.is_draw():
            self.handle_draw()
            return True

        return False

    def handle_game_end(self, winner):
        # NEW: count losses only in AI mode
        if not self.pvp_mode and winner == "O":
            self.losses += 1
            self.update_stats()

        QMessageBox.information(self, "Game Over", f"Player {winner} wins!")
        self.reset_game()

    def handle_draw(self):
        # NEW: count draws only in AI mode
        if not self.pvp_mode:
            self.draws += 1
            self.update_stats()

        QMessageBox.information(self, "Game Over", "It's a Draw!")
        self.reset_game()

    # NEW
    def update_stats(self):
        self.stats_label.setText(f"Losses: {self.losses} | Draws: {self.draws}")

    def ai_move(self):
        best_val = -float('inf')
        move = None

        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    self.board[r][c] = "O"
                    score = self.minimax(self.board, False)
                    self.board[r][c] = ""
                    if score > best_val:
                        best_val = score
                        move = (r, c)

        if move:
            self.make_move(move[0], move[1], "O")

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

    def Terminal(self, b, p):
        wins = [
            [b[0][0], b[0][1], b[0][2]], [b[1][0], b[1][1], b[1][2]], [b[2][0], b[2][1], b[2][2]],
            [b[0][0], b[1][0], b[2][0]], [b[0][1], b[1][1], b[2][1]], [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]
        ]
        return [p, p, p] in wins

    def check_winner(self, p):
        return self.Terminal(self.board, p)

    def is_draw(self):
        return not any("" in row for row in self.board)

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in self.buttons:
            for btn in row:
                btn.setText("")
                btn.setEnabled(True)
                btn.setStyleSheet(
                    "background-color: #34495e; color: white; font-size: 60px; border-radius: 10px;"
                )
        self.status_label.setText("YOUR TURN (X)" if not self.pvp_mode else "PLAYER X'S TURN")


import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("resources/quizicon.png"))
window = QuizView()
window.show()
sys.exit(app.exec_())