import tkinter as tk

class BouncingBall:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Ball Animation")
        self.width = 400
        self.height = 300
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.ball_radius = 20
        self.x = self.width // 2
        self.y = self.height // 2
        self.dx = 4  # movement in x (pixels per frame)
        self.dy = 3  # movement in y
        self.ball = self.canvas.create_oval(
            self.x - self.ball_radius, self.y - self.ball_radius,
            self.x + self.ball_radius, self.y + self.ball_radius,
            fill="blue"
        )

        self.animate()

    def animate(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off left or right walls
        if self.x - self.ball_radius <= 0 or self.x + self.ball_radius >= self.width:
            self.dx = -self.dx

        # Bounce off top or bottom walls
        if self.y - self.ball_radius <= 0 or self.y + self.ball_radius >= self.height:
            self.dy = -self.dy

        self.canvas.coords(
            self.ball,
            self.x - self.ball_radius, self.y - self.ball_radius,
            self.x + self.ball_radius, self.y + self.ball_radius
        )

        # Call this method again after 20 milliseconds (50 FPS)
        self.root.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = BouncingBall(root)
    root.mainloop()
