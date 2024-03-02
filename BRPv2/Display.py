import tkinter
import customtkinter
import os
import ctypes

from PIL import Image, ImageTk
from tkinter import messagebox

from Defaults import Defaults

global main_window
global brp_official_logo


def display_main_menu_old():
    window_title = "Interaktywna karta postaci w systemie BRP"
    header_text = "Tworzenie postaci w systemie BRP"
    text1 = "Wyświetlanie"
    text2 = "Tworzenie"
    text3 = "Opcje"
    text4 = "Wyjście"
    footer_text = "To oprogramowanie opiera się na zasadach gry udostępnionych\nprzez Chaosium Inc. zgodnie z licencją BRP Open Game License, Version 1.0."
    my_width = 20

    clear_main_window()
    main_window.title(window_title)

    header = tkinter.Frame(background=Defaults.default_bg_color)
    header.pack()
    tkinter.Label(header, text=header_text, font=Defaults.default_header1_font,
                  background=Defaults.default_bg_color).grid(
        row=0, column=0, pady=20, )

    body = tkinter.Frame(background=Defaults.default_bg_color)
    body.pack()
    tkinter.Button(body, text=text1, command=blank, width=my_width, font=Defaults.default_text_font).grid(row=1,
                                                                                                          column=0,
                                                                                                          pady=20)
    tkinter.Button(body, text=text2, command=blank, width=my_width, font=Defaults.default_text_font).grid(row=2,
                                                                                                          column=0,
                                                                                                          pady=20)
    tkinter.Button(body, text=text3, command=blank, width=my_width, font=Defaults.default_text_font).grid(row=3,
                                                                                                          column=0,
                                                                                                          pady=20)
    tkinter.Button(body, text=text4, command=display_exit, width=my_width, font=Defaults.default_text_font).grid(row=4,
                                                                                                                 column=0,
                                                                                                                 pady=20)

    footer = tkinter.Frame(background=Defaults.default_bg_color)
    footer.pack(side=tkinter.BOTTOM, pady=10)
    try:
        global brp_official_logo
        brp_official_logo = ImageTk.PhotoImage(
            Image.open(os.path.join(Defaults.default_path_images, 'BRP_logo.png')).resize((100, 100)))
        tkinter.Label(footer, image=brp_official_logo, bg=Defaults.default_bg_color).grid(row=0, column=0, padx=10)
    except FileNotFoundError:
        print("File not found")
    bottom_label = tkinter.Label(footer, text=footer_text, font=Defaults.default_text_font,
                                 bg=Defaults.default_bg_color)
    bottom_label.grid(row=0, column=1, padx=10)


def display_main_menu():
    clear_main_window()
    main_window.title("Interaktywna karta postaci w systemie BRP")

    body = tkinter.Frame(background=Defaults.default_bg_color)
    body.pack()
    (customtkinter.CTkButton(body, text="Wyświetlanie", command=blank)
     .grid(row=1, column=0, pady=5, padx=5))
    (customtkinter.CTkButton(body, text="Tworzenie", command=blank)
     .grid(row=2, column=0, pady=5, padx=5))
    (customtkinter.CTkButton(body, text="Zmień motyw", command=change_color)
     .grid(row=3, column=0, pady=5, padx=5))
    (customtkinter.CTkButton(body, text="Wyjście", command=display_exit)
     .grid(row=4, column=0, pady=5, padx=5))


def display_creation():
    pass


def display_selection():
    pass


def display_character():
    pass


def display_exit():
    if messagebox.askyesno("Wyjście", "Czy na pewno chcesz wyjść?"):
        main_window.destroy()


def change_color():
    Defaults.switch_color(Defaults)
    main_window.configure(bg=Defaults.default_bg_color)
    display_main_menu()


def create_window():
    try:
        global main_window
        main_window = tkinter.Tk()
        set_window_def_params()
        display_main_menu()
        main_window.mainloop()
        return True
    except ValueError:
        return False


def clear_main_window():
    for widget in main_window.winfo_children():
        widget.destroy()


def set_window_def_params():
    main_window.geometry("800x600")
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    main_window.minsize(800, 600)
    main_window.configure(bg=Defaults.default_bg_color)


def blank():
    pass  # empty function for buttons use
