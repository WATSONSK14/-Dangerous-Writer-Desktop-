from tkinter import *
from utils import Utils

class AuthorExercise:
    def __init__(self, window):
        # -------- Ekran Ayarları --------
        self.window = window
        self.window.title("AuthorExercise")
        window_width = 1200
        window_height = 900
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2) -50
        self.window.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
        self.window.resizable(False, False)
        # -------- Frames --------
        self.m_page = Frame(self.window, bg="#1f2024")
        self.m_page.pack(fill="both", expand=True)
        # -------- Utils --------
        self.utils = Utils(self.window, self.m_page, self.start_game)
        self.start_game()

    def start_game(self):
        self.utils.placeholder()
        if hasattr(self.utils, "canvas") and hasattr(self.utils, "button") and hasattr(self.utils, "label"):
            self.utils.restart_destroy()
        self.utils.textarea()
        self.utils.events()
        self.utils.countdown()

        self.check_game()

    def check_game(self):
        if self.utils.go:
            self.utils.word_control()
            self.utils.area.destroy()
            self.utils.create_final_widget()
        else:
            self.window.after(50, self.check_game)




window = Tk()
app = AuthorExercise(window)
window.mainloop()