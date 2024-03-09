import os


class Defaults:
    class Params:
        window_min_x: int = 800
        window_min_y: int = 600

    class Styles:
        header1_font: tuple[str, int, str] = ("Arial", 20)
        header2_font: tuple[str, int, str] = ("Arial", 16)
        text_font: tuple[str, int, str] = ("Arial", 13)

    class Paths:
        images = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Images')
        sheets = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'SheetsOfCharacters')

    class Links:
        webpage_chaousim = r"https://www.chaosium.com/content/FreePDFs/BRP/BRP%20SRD%20-%20V1.0.pdf"
