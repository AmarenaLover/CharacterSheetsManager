import customtkinter as ctk
import webbrowser as wb
from Defaults import Defaults

global color


class DefaultParameters:
    def __init__(self):
        self.color = True

    def change_theme(self):
        self.color = not self.color
        if self.color:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    @staticmethod
    def show_webpage_chaousium():
        wb.open_new(Defaults.Links.webpage_chaousim)

    @staticmethod
    def count_character_sheets():
        pass
