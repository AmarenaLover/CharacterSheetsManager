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
        # self.display_test_window()
        self.display_main_menu()
        self.main_window.mainloop()

    def display_exit(self):
        if messagebox.askyesno("Wyjście", "Czy na pewno chcesz wyjść?"):
            self.main_window.destroy()

    def clear_main_window(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()

    def display_main_menu(self):
        self.clear_main_window()
        # HEAD PART
        Ve.CreateHeader(self.main_window,
                        head_name="INTERAKTYWNA KARTA POSTACI").pack()
        # HEAD PART

        # BODY PART
        body = ctk.CTkFrame(self.main_window)
        body.pack(ipadx=5, ipady=0)

        Ve.CreateButton(body,
                        button_text="Wyświetl postać",
                        button_command=self.display_character_selection)
        Ve.CreateButton(body,
                        button_text="Stwórz postać",
                        button_command=None)
        Ve.CreateButton(body,
                        button_text="Zmień motyw",
                        button_command=self.op.change_theme)
        Ve.CreateButton(body,
                        button_text="Wyjście",
                        button_command=self.display_exit)
        # BODY PART

        # FOOT PART
        Ve.CreateMainMenuFooter(self.main_window,
                                img_button_command=self.op.show_webpage_chaousium)
        # FOOT PART

    def display_character_selection(self):
        self.clear_main_window()

        # HEAD PART
        Ve.CreateHeader(self.main_window,
                        head_name="WYBÓR POSTACI").pack()
        # HEAD PART

        # BODY PART
        body = ctk.CTkFrame(self.main_window)
        body.pack(padx=5, pady=5,
                  side=ctk.TOP)

        Ve.CreateCharacterSelectionRow(master=body, character_name="Dawid Grzelka").pack()
        Ve.CreateCharacterSelectionRow(master=body, character_name="Dawid Grzelka Dawid Grzelka").pack()

        # BODY PART

        # FOOT PART
        foot = ctk.CTkFrame(self.main_window)
        foot.pack(padx=5, pady=5,
                  ipadx=5, ipady=0,
                  side=ctk.BOTTOM)
        Ve.CreateButton(foot,
                        button_text="Cofnij do menu",
                        button_command=self.display_main_menu,
                        button_padding_color=foot.fg_color).pack(side=ctk.LEFT,
                                                               expand=True)
        # FOOT PART

    def display_test_window(self):
        Ve.CreateHeader(self.main_window)
        # body = ctk.CTkFrame(self.main_window,
        #                     fg_color="red")
        # body.pack()
        Ve.CreateButton(self.main_window)
        # Ve.CreateButton(body)