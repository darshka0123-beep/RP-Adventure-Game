import time
import tkinter as tk
import pygame

# Initialize Pygame audio player
pygame.mixer.init()
pygame.mixer.music.load("bad.mp3")

# Time stamps in seconds matched with lyric lines
# "bad" by wave to earth is a calm indie-pop track about how spending time with someone special can
# can easily turn a boring muddy day 180 degrees around.
# Update numbers to match second on mp3 file
LYRICS = [
    (1.0, "how could my day be bad when i'm with you?"), 
    (7.5, "you're the only one who makes me laugh!"),
    (13.5, "so how can my day be bad?"),
    (20.5, "it's a day for youuuu"),
    (30.5, "lately, life's so boring"),
    (35, "i've been watching netflix all day long :("),
    (41.5, "i thought there would be"),
    (45.5, "no things left to watch"),
    (48.5, "so i let myself out."),
    (57.5, "when i went to the park"),
    (62.5, "i recognized you at a glance"),
    (70.5, "face to face, we just smiled"),
    (75.5, "we already know that we'll be together"),
    (82.5, "(we'll be togetherrr)"),
    (87, "how could my day be bad when i'm with you?"),
    (91.5, "you're the only one who makes me laugh!"),
    (98.5, "so how can my day be bad?"),
    (105, "it's a day for you"),
    (110, "oh, babe"),
    (117, "coffee in the morning"),
    (120, "you and the sun!"),
    (124, "there's a brown hue in your eyes")
    (131, "how pretty it is?"),
    ()

]

# Visual Styling for the floating lyric cards
BOX_W, BOX_H = 350, 260
FONT = ("Helvetica", 25, "italic") 
BG_COLOR = "#E22D8E"
FG_COLOR = "#FFFFFF"
RISE_SPEED = 60

class LyricCard:
    def __init__(self, parent, text, x, y):
        self.win = tk.Toplevel(parent)
        self.win.overrideredirect(True)
        self.win.attributes("-topmost", True)
        self.win.configure(bg=BG_COLOR)
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(x)}+{int(y)}")

        self.full_text = text
        self.label = tk.Label(
            self.win,
            text="",
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
        self.screen_h = root.winfo_screenheight()

        self.next_lyric_idx = 0
        self.cards = []
        self.last_frame_time = None
        self.current_side = "left"

        pygame.mixer.music.play()
        self.start_time = time.time()
        self.update_loop()

    def get_x_position(self):
        if self.current_side == "left":
            self.current_side = "right"
            return self.screen_w // 6
        else:
            self.current_side = "left"
            return (self.screen_w // 2) + 100

    def update_loop(self):
        now = time.time()
        elapsed = now - self.start_time

        if self.next_lyric_idx < len(LYRICS):
            t, text = LYRICS[self.next_lyric_idx]
            if elapsed >= t:
                x = self.get_x_position()
                y = self.screen_h - BOX_H - 100
                card = LyricCard(self.root, text, x, y)
                self.cards.append(card)
                self.next_lyric_idx += 1

        if self.last_frame_time:
            dt = now - self.last_frame_time
            dy = RISE_SPEED * dt
            for card in self.cards:
                card.rise(dy)
        self.last_frame_time = now
        self.root.after(20, self.update_loop)


if __name__ == "__main__":
    root = tk.Tk()
    app = LyricFloatApp(root)
    root.mainloop 




        