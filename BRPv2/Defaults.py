import os


class Defaults:
    default_header1_font: tuple[str, int, str] = ("Arial", 20)
    default_header2_font: tuple[str, int, str] = ("Arial", 14, 'bold')
    default_text_font: tuple[str, int, str] = ("Arial", 13)

    default_path_images = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Images')

    default_link_webpage_chaousim = r"https://www.chaosium.com/content/FreePDFs/BRP/BRP%20SRD%20-%20V1.0.pdf"