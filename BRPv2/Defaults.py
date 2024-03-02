import os


class Defaults:
    switch = True
    light_bg_color = '#c4c4c4'
    dark_bg_color = '#3b3b3b'
    default_bg_color = light_bg_color

    default_header1_font: tuple[str, int, str] = ("Arial", 19, 'bold')
    default_header2_font: tuple[str, int, str] = ("Arial", 14, 'bold')
    default_text_font: tuple[str, int, str] = ("Arial", 10)

    default_path_images = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Images')

    def switch_color(self):
        self.switch = not self.switch
        if self.switch:
            self.default_bg_color = self.light_bg_color
        else:
            self.default_bg_color = self.dark_bg_color
