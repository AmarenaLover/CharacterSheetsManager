import customtkinter as ctk
import Defaults
import os
from PIL import Image
from Defaults import Defaults


class CreateHeader(ctk.CTkFrame):
    def __init__(self,
                 *args,
                 head_name='Brak nagłówka',
                 **kwargs):
        super().__init__(*args,
                         **kwargs)

        self.pack(padx=5, pady=5,
                  ipadx=5, ipady=5,
                  fill=ctk.X)

        ctk.CTkLabel(master=self,
                     text=head_name,
                     font=Defaults.Styles.header1_font).pack(expand=True)


class CreateButton(ctk.CTkFrame):
    def __init__(self,
                 *args,
                 button_text='Brak nazwy',
                 button_command=None,
                 button_padding_color='transparent',
                 **kwargs):
        super().__init__(*args,
                         **kwargs)

        self.configure(fg_color=button_padding_color)

        self.pack(expand=True)

        ctk.CTkButton(master=self,
                      text=button_text,
                      command=button_command).pack(padx=5, pady=5, ipadx=5, ipady=5)


class CreateImage(ctk.CTkFrame):
    def __init__(self,
                 *args,
                 img_name=None,
                 img_command=None,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.pack(padx=5, pady=5, expand=False)

        img = ctk.CTkImage(dark_image=Image.open(os.path.join(Defaults.Paths.images, img_name)),
                           size=(90, 90))

        ctk.CTkButton(self,
                      text="",
                      image=img,
                      width=10,
                      command=img_command,
                      fg_color=self._fg_color).pack(ipadx=5, ipady=5)


class CreateMainMenuFooter(ctk.CTkFrame):
    def __init__(self,
                 *args,
                 img_button_name="BRP_logo.png",
                 img_button_command=None,
                 footer_text_color="gray14",
                 **kwargs):
        super().__init__(*args,
                         **kwargs)

        self.pack(side=ctk.BOTTOM,
                  padx=5, pady=5,
                  fill=ctk.X)

        CreateImage(self,
                    fg_color=self._fg_color,
                    img_name=img_button_name,
                    img_command=img_button_command,
                    ).pack(side=ctk.LEFT)

        ctk.CTkLabel(self,
                     text='To oprogramowanie opiera się na zasadach gry udostępnionych przez Chaosium Inc. zgodnie z licencją BRP Open Game License, Version 1.0.',
                     wraplength=600,
                     text_color=footer_text_color,
                     font=Defaults.Styles.text_font).pack(expand=True,
                                                          padx=10, pady=5)


class CreateCharacterSelectionRow(ctk.CTkFrame):
    def __init__(self,
                 *args,
                 character_name="Brak imienia",
                 character_file_name=None,  # will be used later to open proper character scheet
                 **kwargs):
        super().__init__(*args,
                         **kwargs)

        self.configure(width=500)
        self.pack(padx=5, pady=5,
                  ipadx=5, ipady=5)

        CreateCharacterSelectionRowCharacter(master=self,
                                             name=character_name).pack()

        CreateButton(self,
                     button_text="Wyświetl",
                     button_command=None)


class CreateCharacterSelectionRowCharacter(ctk.CTkFrame):
    def __init__(self,
                 *args,
                 name,
                 background_color="transparent",
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color=background_color)
        self.pack(side=ctk.LEFT)

        ctk.CTkLabel(master=self,
                     width=400,
                     font=Defaults.Styles.header2_font,
                     fg_color=background_color,
                     text=name).pack(expand=True)
