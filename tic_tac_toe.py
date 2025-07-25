import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.game_over = False
        self.board = [[None]*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        
        self.create_widgets()

    def create_widgets(self):
        self.status_label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=(10,0))

        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2,
                                command=lambda row=r, col=c: self.on_click(row, col))
                btn.grid(row=r+1, column=c, padx=5, pady=5)
                self.buttons[r][c] = btn

        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 14), command=self.reset_board)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=(10,10))

    def on_click(self, row, col):
        if self.game_over:
            return
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player

            if self.check_winner():
                self.game_over = True
                self.highlight_winner()
                self.status_label.config(text=f"Player {self.current_player} wins! 🎉")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif self.is_board_full():
                self.game_over = True
                self.status_label.config(text="It's a tie! 🤝")
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        b = self.board
        p = self.current_player

        # Check rows, columns, and diagonals
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] == p:
                self.winning_line = [(i, 0), (i, 1), (i, 2)]
                return True
            if b[0][i] == b[1][i] == b[2][i] == p:
                self.winning_line = [(0, i), (1, i), (2, i)]
                return True

        if b[0][0] == b[1][1] == b[2][2] == p:
            self.winning_line = [(0,0), (1,1), (2,2)]
            return True
        if b[0][2] == b[1][1] == b[2][0] == p:
            self.winning_line = [(0,2), (1,1), (2,0)]
            return True

        self.winning_line = []
        return False

    def highlight_winner(self):
        for r, c in self.winning_line:
            self.buttons[r][c].config(bg="lightgreen")

    def is_board_full(self):
        return all(all(cell is not None for cell in row) for row in self.board)

    def reset_board(self):
        self.board = [[None]*3 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", bg="SystemButtonFace")
        self.current_player = "X"
        self.game_over = False
        self.status_label.config(text=f"Player {self.current_player}'s turn")

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    game = TicTacToe(root)
    root.mainloop()

else : 
    print("ffff")