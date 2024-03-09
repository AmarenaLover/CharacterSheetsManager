import customtkinter as ctk
import Defaults
import os
from PIL import Image
from Defaults import Defaults


class CreateHeader(ctk.CTkFrame):
    def __init__(self, *args, head_name, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(padx=5, pady=5,
                  ipadx=5, ipady=5,
                  fill=ctk.X)
        ctk.CTkLabel(master=self,
                     text=head_name,
                     font=Defaults.default_header1_font).pack(expand=True)


class CreateButton(ctk.CTkFrame):
    def __init__(self, *args, button_text, button_command, button_frame_color, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color=button_frame_color)

        ctk.CTkButton(master=self,
                      text=button_text,
                      command=button_command).pack(padx=5,
                                                   pady=5,
                                                   ipadx=5,
                                                   ipady=5)


class CreateImage(ctk.CTkFrame):
    def __init__(self, *args, img_name, img_command=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack(padx=5, pady=5, expand=False)

        img = ctk.CTkImage(light_image=Image.open(os.path.join(Defaults.default_path_images, img_name)),
                           dark_image=Image.open(os.path.join(Defaults.default_path_images, img_name)),
                           size=(90, 90))

        ctk.CTkButton(self,
                      text="",
                      image=img,
                      width=10,
                      command=img_command,
                      fg_color=self.fg_color).pack(ipadx=5, ipady=5)


class CreateMainMenuFooter(ctk.CTkFrame):
    def __init__(self, *args, img_button_name, img_button_command=None, footer_text_color, footer_background_color,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color=footer_background_color)

        self.pack(side=ctk.BOTTOM,
                  padx=5, pady=5)

        CreateImage(self,
                    fg_color=footer_background_color,
                    img_name=img_button_name,
                    img_command=img_button_command,
                    ).pack(side=ctk.LEFT)

        ctk.CTkLabel(self,
                     text="To oprogramowanie opiera się na zasadach gry udostępnionych przez Chaosium Inc. zgodnie z licencją BRP Open Game License, Version 1.0.",
                     wraplength=600,
                     text_color=footer_text_color,
                     font=Defaults.default_text_font).pack(expand=True,
                                                           padx=10, pady=5)
