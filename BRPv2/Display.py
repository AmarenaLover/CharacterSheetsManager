# import ctypes

import os
from PIL import Image
from Defaults import Defaults
import customtkinter as ctk
from tkinter import messagebox

class Display:
    def __init__(self):
        self.main_window = ctk.CTk()
        self.main_window.title("BRP")
        self.main_window.geometry("800x600")
        self.main_window.minsize(800, 600)
        self.display_main_menu()
        self.main_window.mainloop()

    def display_exit(self):
        if messagebox.askyesno("Wyjście", "Czy na pewno chcesz wyjść?"):
            self.main_window.destroy()

    def display_main_menu(self):
        # HEAD PART
        CreateHeader(self.main_window,
                     fg_color=self.main_window.fg_color,
                     head_name="INTERAKTYWNA KARTA POSTACI").pack(fill=ctk.X)
        # HEAD PART

        # BODY PART
        body = ctk.CTkFrame(self.main_window,
                            fg_color=self.main_window.fg_color)
        body.pack()

        CreateButton(body, fg_color=self.main_window.fg_color, my_text="Wyświetl postać", my_command=blank).pack()
        CreateButton(body, fg_color=self.main_window.fg_color, my_text="Stwórz postać", my_command=blank).pack()
        CreateButton(body, fg_color=self.main_window.fg_color, my_text="Zmień motyw", my_command=blank).pack()
        CreateButton(body, fg_color=self.main_window.fg_color, my_text="Wyjście", my_command=self.display_exit).pack()
        # BODY PART

        # FOOT PART
        foot = ctk.CTkFrame(self.main_window)
        foot.pack(side=ctk.BOTTOM,
                  padx=5, pady=5,
                  expand=False,
                  fill=ctk.X)
        CreateImage(foot,
                    # fg_color=foot.fg_color,
                    img_name="BRP_logo.png").pack(padx=5, pady=5,
                                                  ipadx=5, ipady=5,
                                                  expand=False,
                                                  side=ctk.LEFT)
        (ctk.CTkLabel(foot,
                      text="To oprogramowanie opiera się na zasadach gry udostępnionych przez Chaosium Inc. zgodnie z licencją BRP Open Game License, Version 1.0.",
                      wraplength=220,
                      # text_color=foot.fg_color,
                      font=Defaults.default_text_font)
         .pack(expand=False,
               side=ctk.RIGHT,
               padx=10, pady=5))
        # FOOT PART


class CreateHeader(ctk.CTkFrame):
    def __init__(self, *args, head_name, **kwargs):
        super().__init__(*args, **kwargs)
        head = ctk.CTkFrame(self)
        head.pack(side=ctk.TOP,
                  padx=5, pady=5,
                  ipadx=5, ipady=5,
                  expand=False,
                  fill=ctk.X)
        ctk.CTkLabel(master=head,
                     text=head_name,
                     font=Defaults.default_header1_font).pack(expand=True)


class CreateButton(ctk.CTkFrame):
    def __init__(self, *args, my_text, my_command, **kwargs):
        super().__init__(*args, **kwargs)
        (ctk.CTkButton(master=self,
                       text=my_text,
                       command=my_command)
         .pack(padx=5,
               pady=5,
               ipadx=5,
               ipady=5))


class CreateImage(ctk.CTkFrame):
    def __init__(self, *args, img_name, **kwargs):
        super().__init__(*args, **kwargs)
        img = ctk.CTkImage(light_image=Image.open(os.path.join(Defaults.default_path_images, img_name)),
                           dark_image=Image.open(os.path.join(Defaults.default_path_images, img_name)),
                           size=(85, 85))
        ctk.CTkLabel(self,
                     text="",
                     image=img,
                     padx=5, pady=5).pack()


# def clear_main_window():
#     for widget in main_window.winfo_children():
#         widget.destroy()


def blank():
    pass  # empty function for buttons use
