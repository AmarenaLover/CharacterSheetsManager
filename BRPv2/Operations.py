import customtkinter as ctk
import webbrowser as wb
from Defaults import Defaults

def change_theme():
    ctk.set_appearance_mode("light")

def show_webpage_chaousium():
    wb.open_new(Defaults.default_link_webpage_chaousim)