import customtkinter as ctk
from tkinter import messagebox

from Operations import DefaultParameters

import ViewElements as Ve


class View:
    def __init__(self):
        self.main_window = ctk.CTk()
        self.op = DefaultParameters()

        self.main_window.title("BRP")
        self.main_window.geometry("800x600")
        self.main_window.minsize(800, 600)
        self.display_main_menu()
        self.main_window.mainloop()

    def display_exit(self):
        if messagebox.askyesno("Wyjście", "Czy na pewno chcesz wyjść?"):
            self.main_window.destroy()

    def clear_main_window(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()

    def display_main_menu(self):
        # HEAD PART
        Ve.CreateHeader(self.main_window,
                        head_name="INTERAKTYWNA KARTA POSTACI").pack()
        # HEAD PART

        # BODY PART
        body = ctk.CTkFrame(self.main_window,
                            fg_color=self.main_window.fg_color)
        body.pack()

        Ve.CreateButton(body,
                        button_text="Wyświetl postać",
                        button_command=None,
                        button_frame_color=self.main_window.fg_color).pack()
        Ve.CreateButton(body,
                        button_text="Stwórz postać",
                        button_command=None,
                        button_frame_color=self.main_window.fg_color).pack()
        Ve.CreateButton(body,
                        button_text="Zmień motyw",
                        button_command=self.op.change_theme,
                        button_frame_color=self.main_window.fg_color).pack()
        Ve.CreateButton(body,
                        button_text="Wyjście",
                        button_command=self.display_exit,
                        button_frame_color=self.main_window.fg_color).pack()
        # BODY PART

        # FOOT PART
        foot = ctk.CTkFrame(self.main_window)
        foot.pack(fill=ctk.X,
                  padx=5, pady=5,
                  side=ctk.BOTTOM)

        Ve.CreateMainMenuFooter(foot,
                                img_button_name="BRP_logo.png",
                                img_button_command=self.op.show_webpage_chaousium,
                                footer_text_color=self.main_window.fg_color,
                                footer_background_color=foot.fg_color).pack()
        # FOOT PART
