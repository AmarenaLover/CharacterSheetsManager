import os


class Defaults:
    default_color = "grey"
    default_header1_font: tuple[str, int, str] = ("Arial", 19, 'bold')
    default_header2_font: tuple[str, int, str] = ("Arial", 14, 'bold')
    default_text_font: tuple[str, int, str] = ("Arial", 10)
    default_path_images = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Images')
