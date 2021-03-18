from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.platypus import Table
from random import uniform, randint, choice


def get_path(path: str):
    """
    This function checks path for errors and returning new path\n
    :param path: assigned path to file
    """
    if path[len(path) - 1] != '/' and ".pdf" not in path:
        path += '/'
    elif ".pdf" in path:
        path = path[0:path.rfind('/') + 1:1]
    path += "generated.pdf"
    return path


def create_file(path: str):
    """
    This function create pdf-file\n
    :param path: path for create file (e.g. c:/files/)
    """
    file = Canvas(get_path(path))
    file.setAuthor("PDF_generator")
    file.setTitle("Generated pdf")
    file.save()


def set_font(path: str, font_size: int):
    """
    This function set up font and his size in file\n
    :param path: path to file (e.g. c:/files/)
    :param font_size: size of font
    """
    using_font = ttfonts.TTFont("Calibri", "Calibri.ttf")
    pdfmetrics.registerFont(using_font)
    file = Canvas(get_path(path))
    file.setFont("Calibri", font_size)
    file.save()


def write_text(path: str, text: str, position: str = "mid", x: float = 297.635, y: float = 815.89):
    """"
    This function write text on defined position\n
    size of page is 595.27,841.89
    :param path: path to file (e.g. c:/files/)
    :param text: string of text to writing
    :param position: left/mid/right position of string of text
    :param x, y: coordinates of string
    """
    file = Canvas(get_path(path))
    if position == "left":
        file.drawString(x, y, text)
    elif position == "mid":
        file.drawString(x, y, text)
    elif position == "right":
        file.drawRightString(x, y, text)
    file.save()


def random_drawing(path: str, fg_count: int):
    """
    This function draws random picture\n
    :param path: path to file (e.g. c:/files/)
    :param fg_count: count of figures, drawn on page
    """
    file = Canvas(get_path(path))
    file.setFillColorRGB(uniform(0, 1), uniform(0, 1), uniform(0, 1), alpha=uniform(0, 1))
    file.setStrokeColorRGB(uniform(0, 1), uniform(0, 1), uniform(0, 1), alpha=uniform(0, 1))
    file.rect(100, 100, 395.27, 641, fill=randint(0, 1))
    for figure in range(fg_count):
        methods = [file.bezier(randint(100, 495), randint(100, 741), randint(100, 495), randint(100, 741),
                               randint(100, 495), randint(100, 741), randint(100, 495), randint(100, 741), ),
                   file.arc(randint(100, 495), randint(100, 741), randint(100, 495), randint(100, 741)),
                   file.rect(randint(100, 395), randint(100, 641), randint(1, 100), randint(1, 100),
                             fill=randint(0, 1)),
                   file.ellipse(randint(100, 495), randint(100, 741), randint(100, 495), randint(100, 741),
                                fill=randint(0, 1)),
                   file.circle(randint(100, 395), randint(100, 641), randint(1, 100), fill=randint(0, 1)),
                   file.roundRect(randint(100, 395), randint(100, 641), randint(1, 100), randint(1, 100),
                                  randint(1, 100), fill=randint(0, 1))]
        file.setFillColorRGB(uniform(0, 1), uniform(0, 1), uniform(0, 1), alpha=uniform(0, 1))
        file.setStrokeColorRGB(uniform(0, 1), uniform(0, 1), uniform(0, 1), alpha=uniform(0, 1))
        choice(methods)
    file.save()


def draw_table(path: str, data: list):
    """
    This function draws random table\n
    :param path: path to file (e.g. c:/files/)
    :param data: list with data for table, e.g.
            [[" ", "function", "count of strings"],
            [1, "get_path", 10],
            [2, "create_file", 8],
            [3, "set_font", 10],
            [4, "random_drawing", 23]]
    """
    file = Canvas(get_path(path))
    table = Table(data=data, style=[("INNERGRID", (0, 0), (-1, -1), 1, "Black"), ("BOX", (0, 0), (-1, -1), 1, "Black")])
    table.wrapOn(file, 10, 10)
    table.drawOn(file, 10, 10)
    file.save()



