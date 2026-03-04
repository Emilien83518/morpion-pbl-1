import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, 
                             QPushButton, QMessageBox, QApplication, QComboBox, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion AI")
        self.setFixedSize(600, 800) # Increased height for menu and stats
        self.setStyleSheet("background-color: #2c3e50;") 

        # Game State Variables
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.loss_streak = 0
        self.game_mode = "Player vs AI" # Default mode

        # UI Elements: Top Menu
        self.menu_layout = QHBoxLayout()
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Player vs AI", "Player vs Player"])
        self.mode_selector.setStyleSheet("""
            QComboBox { 
                background-color: #34495e; color: white; padding: 5px; 
                font-size: 16px; border-radius: 5px; min-width: 200px;
            }
        """)
        self.mode_selector.currentTextChanged.connect(self.change_mode)
        self.menu_layout.addWidget(QLabel("<font color='white'>Mode:</font>"))
        self.menu_layout.addWidget(self.mode_selector)
        self.menu_layout.addStretch()

        # UI Elements: Status and Streak
        self.status_label = QLabel("YOUR TURN (X)", self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold; margin: 10px;")

        self.streak_label = QLabel("Loss Streak vs AI: 0", self)
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
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #34495e; 
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
        main_layout.addWidget(self.streak_label)
        self.setLayout(main_layout)

    def change_mode(self, mode):
        self.game_mode = mode
        self.reset_game()

    def handle_click(self, r, c):
        if self.board[r][c] == "":
            if self.game_mode == "Player vs AI":
                # Original AI Logic
                if self.make_move(r, c, "X"):
                    return 
                
                self.status_label.setText("AI IS THINKING...")
                self.status_label.repaint() 
                self.ai_move()
            else:
                # PvP Logic
                self.make_move(r, c, self.current_player)
                self.current_player = "O" if self.current_player == "X" else "X"
                if not self.is_draw() and not self.check_winner("X") and not self.check_winner("O"):
                    self.status_label.setText(f"PLAYER {self.current_player} TURN")

    def make_move(self, row, col, player):
        self.board[row][col] = player
        self.buttons[row][col].setText(player)
        self.buttons[row][col].setEnabled(False)
        
        color = "#e74c3c" if player == "X" else "#f1c40f"
        self.buttons[row][col].setStyleSheet(f"background-color: #34495e; color: {color}; font-size: 60px; border-radius: 10px;")

        if self.check_winner(player):
            if self.game_mode == "Player vs AI":
                if player == "O":
                    self.loss_streak += 1
                else:
                    self.loss_streak = 0 # Reset streak if player wins
                self.streak_label.setText(f"Loss Streak vs AI: {self.loss_streak}")
            
            self.end_game(f"Player {player} wins!")
            return True

        if self.is_draw():
            self.end_game("It's a Draw!")
            return True
        
        self.status_label.setText("YOUR TURN (X)" if player == "O" else "AI'S TURN (O)")
        return False

    # --- MINIMAX LOGIC (UNCHANGED) ---
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
                btn.setStyleSheet("background-color: #34495e; color: white; font-size: 60px; border-radius: 10px;")
        self.status_label.setText("YOUR TURN (X)" if self.game_mode == "Player vs AI" else "PLAYER X TURN")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizView()
    window.show()
    sys.exit(app.exec_())