from tkinter import *
from PIL import Image, ImageTk
import os, sys



class Utils:
    def __init__(self, window, m_page, start_game):
        self.window = window
        self.m_page = m_page
        self.start_game = start_game
        self.placeholder()

    def relative_path(self, filename):
        try:
            base_path = sys._MEIPASS  # PyInstaller çalışma klasörü
        except Exception:
            base_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, filename)

    def placeholder(self):
        self.time = 1000
        self.font = ("Arial", 18)
        self.son_index = "1.0"
        self.full_text = None
        self.words = []
        self.go = False
        self.label_text = 0
        self.last_word = ""

    def events(self):
        self.area.bind("<KeyPress>", self.start_write)
        self.area.bind("<space>", self.word_count)

    def downland_text(self):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop", "article.txt")
        with open(desktop, "w", encoding="utf-8") as file:
            file.write(self.full_text)

    def restart_destroy(self):
        self.canvas.destroy()
        self.label.destroy()
        self.button.destroy()

    def textarea(self):
        self.area = Text(self.m_page, bg="#ffffff", font=self.font)
        self.area.pack(fill="both", expand=True)
        self.area.place(x=250, y=40, width=700, height=850)
        self.area.focus_set()



    def create_final_widget(self):

        cnv_img = Image.open(self.relative_path("images/canvas.png")).resize((700, 500))
        self.cnvs_img = ImageTk.PhotoImage(cnv_img)

        self.canvas = Canvas(self.m_page)
        self.canvas.create_image(0, 0, image=self.cnvs_img, anchor="nw")
        self.canvas.place(x=270, y=120, width=700, height=500)

        self.label = Button(self.canvas, text=f"{self.label_text}", font=self.font, bg="#023230", fg="#ffffff", command=self.downland_text)
        self.label.place(x=174, y=418, width=155, height=70)

        self.button = Button(self.canvas, text="Restart", font=self.font, bg="#023230", fg="#ffffff", command=self.start_game)
        self.button.place(x=373, y=418, width=155, height=70)


    def word_count(self, event):
        kelime = self.area.get(self.son_index, "insert").strip()
        self.words.append(kelime)
        self.son_index = self.area.index("insert")

    def start_write(self, event):
        self.time = 5

    def countdown(self):
        if self.time > 0:
            self.time -= 1
            self.window.after(1000, self.countdown)
        else:
            self.full_text = self.area.get("1.0", END)
            self.last_word = self.area.get(self.son_index, "insert").strip()
            self.words.append(self.last_word)
            self.area.delete("1.0", END)
            self.go = True

    def word_control(self):
        for word in self.words:
            if len(word) > 1:
                self.label_text += 1