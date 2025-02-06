# ui/widgets.py
import tkinter as tk


class RoundedButton(tk.Canvas):
    def __init__(self, master, text="", command=None, width=120, height=40, bg="#61dafb", fg="#f8f9fa"):
        super().__init__(master, width=width, height=height, bg=bg, highlightthickness=0)
        self.command = command
        self.text = text
        self.bg_color = bg
        self.fg_color = fg
        self.radius = 15

        # Bind events
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

        self.draw_button()

    def draw_button(self):
        self.delete("all")
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        # Draw rounded rectangle
        self.create_rounded_rectangle(0, 0, width, height, self.radius, fill=self.bg_color, outline="")
        self.create_text(width // 2, height // 2, text=self.text, fill=self.fg_color, font=("Arial", 12, "bold"))

    def create_rounded_rectangle(self, x1, y1, x2, y2, r, **kwargs):
        self.create_arc(x1, y1, x1 + r * 2, y1 + r * 2, start=90, extent=90, style=tk.PIESLICE, **kwargs)
        self.create_arc(x2 - r * 2, y1, x2, y1 + r * 2, start=0, extent=90, style=tk.PIESLICE, **kwargs)
        self.create_arc(x1, y2 - r * 2, x1 + r * 2, y2, start=180, extent=90, style=tk.PIESLICE, **kwargs)
        self.create_arc(x2 - r * 2, y2 - r * 2, x2, y2, start=270, extent=90, style=tk.PIESLICE, **kwargs)
        self.create_rectangle(x1 + r, y1, x2 - r, y2, **kwargs)
        self.create_rectangle(x1, y1 + r, x2, y2 - r, **kwargs)

    def on_click(self, event):
        if self.command:
            self.command()

    def on_hover(self, event):
        self.bg_color = "#50c6e5"  # Slightly darker blue
        self.draw_button()

    def on_leave(self, event):
        self.bg_color = "#61dafb"
        self.draw_button()
