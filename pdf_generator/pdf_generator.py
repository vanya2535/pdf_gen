from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.platypus import Table
from random import randint


def wrong_path(path: str):
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
    file = Canvas(wrong_path(path))
    file.setAuthor("PDF_generator")
    file.setTitle("Generated pdf")
    file.save()


def set_font(path: str):
    """
    This function set up font and his size in file
    :param path: path to file (e.g. c:/files/)
    """
    using_font = ttfonts.TTFont("Calibri", "calibri.ttf")
    pdfmetrics.registerFont(using_font)
    file = Canvas(wrong_path(path))
    file.setFont("Calibri", 16)
    file.save


def random_drawing(path: str):
    """
    This function draws random picture\n
    :param path: path to file (e.g. c:/files/)
    """
    file = Canvas(wrong_path(path))
    file.rect(100, 100, 395.27, 641.89)
    file.save()


def random_table(path: str):
    """
    This function draws random table\n
    :param path: path to file (e.g. c:/files/)
    """
    file = Canvas(wrong_path(path))

