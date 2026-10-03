import time
import tkinter as tk
import pygame

# Initialize Pygame audio player
pygame.mixer.init()
pygame.mixer.muisc.load("bad.mp3")

# Time stamps in seconds matched with lyric lines
# "bad" by wave to earth is a calm indie-pop track about how spending time with someone special can
# can easily turn a boring muddy day 180 degrees around.
# Update numbers to match second on mp3 file
LYRICS = [
    (2.0, "How could my day be bad when I'm with you?"), 
    (7.5, "You're the only one who makes me laugh"),
]

# Visual Styling for the floating lyric cards
BOX_W, BOX_H = 350, 260
FONT = ("Snell Roundhand", 24, "italic") 
BG_COLOR = "#D87FC6"
FG_COLOR = "#FFFFFF"
RISE_SPEED = 60

class LyricCard:
    def __init__(self, parent, text, x, y):
        self.win = tk.Toplevel(parent)
        slef.win.overrideredirect(True)
        self.win.attributes("-topmost", True)
        self.win.configure(bg=BG_COLOR)
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(x)}+{int(y)}")

        self.full_text = text
        self.label = tk.Label(
            self.win,
            text"",
            font=FONT,
            bg=BG_COLOR,
            fg=FG_COLOR,
            wraplength=BOX_W - 40,
            justify="center",
        )
        self.label.pack(expand=True, fill="both")


        self.x = x
        self.y = float(y)
        self.typewriter_index = 0
        self.typewriter()

    def typewriter(self):
        if self.typewriter_index <= len(self.full_text):
            self.label.config(text=self.full_text[: self.typewriter_index])
            self.typewriter_index += 1
            self.win.after(60, self.typewriter)

    def rise(self, dy):
        self.y -= dy
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(self.x)}+{int(self.y)}")

class LyricFloatApp:

    def __init__(self, root):
        self.root = root
        self.root.withdraw()

        self.screen_w = root.winfo_screenwidth()
        self.screen_h = 