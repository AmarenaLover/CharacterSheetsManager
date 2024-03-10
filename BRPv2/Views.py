import customtkinter as ctk
from tkinter import messagebox

from Operations import SetDefOperations
import ViewElements as Ve
from Defaults import Defaults


class View:
    def __init__(self):
        self.main_window = ctk.CTk()
        self.op = SetDefOperations()
        self.main_window.minsize(Defaults.Params.window_min_x, Defaults.Params.window_min_y)
        self.main_window.title("BRP")

        # self.display_test_window()
        self.display_main_menu()

        self.main_window.mainloop()

    def display_exit(self):
        if messagebox.askyesno("Wyjście", "Czy na pewno chcesz wyjść?"):
            self.main_window.destroy()

    def display_character_counting_result(self):
        characters_nr = self.op.count_character_sheets()
        if characters_nr == 0:
            messagebox.showinfo("Uwaga", "Nie ma postaci w bazie! Należy stworzyć postać!")
        else:
            self.display_character_selection(characters_nr)

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
        body.pack()

        Ve.CreateButton(body,
                        button_text="Wyświetl postać",
                        button_command=self.display_character_counting_result)
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

    def display_character_selection(self, number):
        self.clear_main_window()
        # HEAD PART
        Ve.CreateHeader(self.main_window,
                        head_name="WYBÓR POSTACI").pack()
        # HEAD PART

        # Foot declaration
        foot = ctk.CTkFrame(self.main_window)

        # BODY PART
        body = ctk.CTkScrollableFrame(self.main_window)
        body.pack(side=ctk.TOP,
                  fill=ctk.BOTH,
                  expand=True,
                  padx=5)

        # hours spent debugging this: 1

        frame_color = ctk.CTkFrame(foot).cget('fg_color')
        for x in range(0, number):
            Ve.CreateCharacterSelectionRow(master=body,
                                           fg_color=frame_color,
                                           character_name="Dawid Grzelka Dawid Grzelka")
        # BODY PART

        # FOOT PART
        foot.pack(padx=5, pady=5,
                  side=ctk.BOTTOM,
                  fill=ctk.X)
        foot2 = ctk.CTkFrame(foot,
                             fg_color=foot.fg_color)
        foot2.pack()
        Ve.CreateButton(foot2,
                        button_text="Cofnij do menu",
                        button_command=self.display_main_menu).pack(side=ctk.LEFT)
        Ve.CreateButton(foot2,
                        button_text="Sortuj",
                        button_command=None).pack(side=ctk.LEFT)
        # FOOT PART

    def display_test_window(self):
        Ve.CreateHeader(self.main_window)
        # body = ctk.CTkFrame(self.main_window,
        #                     fg_color="red")
        # body.pack()
        Ve.CreateButton(self.main_window)
        # Ve.CreateButton(body)
