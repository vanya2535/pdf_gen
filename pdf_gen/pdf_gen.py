from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.platypus import Table
from reportlab.platypus.flowables import Image
from random import uniform, randint, choice
from PyPDF2 import PdfFileMerger
import os


class pdf:

    def __init__(self, path: str, name: str = 'generated'):
        """
        Create a pdf-file object\n
        :param path: path to create file
        :param name: name of file
        """
        self.file = Canvas(self._get_path(path, name))
        self.set_font(12)
        self.page = 1

    def _get_path(self, path: str, name: str = 'generated') -> str:
        """
        This function cleans path\n
        :param path: path to create file
        :param name: name of file
        :return: clean path to file
        """
        path = ''.join(symbol for symbol in path.lower() if symbol not in ' <>?"\*')
        while path.count(':') > 1:
            path = path[:path.rfind(':')] + path[path.rfind(':') + 1:]
        while path[len(path) - 1] == ' ':
            path = path[:len(path) - 1]
        if ".pdf" in path:
            path = path[0:path.rfind('/') + 1:1]
        if path[len(path) - 1] != '/':
            path += '/'
        if '.pdf' in name:
            name = name[:name.rfind('.')]
        return path + name + '.pdf'

    def _format_data(self, data: dict) -> list:
        """
        This function processing data and return list of data for create table\n
        :param data: dict of data
        :return: list of data
        """
        new_data = [[data['title']]]
        add_list = []
        value_list = []
        for column_elem in data['columns']:
            add_list.append(column_elem['name'])
            value_list.append(column_elem['value'])
        new_data.append(add_list.copy())
        add_list.clear()
        for row_elem in data['rows']:
            for value in value_list:
                add_list.append(row_elem[value])
            new_data.append(add_list.copy())
            add_list.clear()
        return new_data

    def _normal_color(self):
        self.file.setFillColor('black')
        self.file.setStrokeColor('black')

    def set_font(self, font_size: int):
        """
        This function set up font and his size in file\n
        :param font_size: size of font
        """
        self.font_size = font_size
        using_font = ttfonts.TTFont("Calibri", "Calibri.ttf")
        pdfmetrics.registerFont(using_font)
        self.file.setFont("Calibri", self.font_size)

    def write_text(self, text: str, position: str = "mid", x: int = 297, y: int = 815):
        """"
        This function write text on defined position\n
        size of page is 595,841\n
        :param text: string of text to writing
        :param position: left/mid/right position of string of text
        :param x, y: coordinates of string
        """
        self._normal_color()
        if position == "left":
            self.file.drawString(x, y, text)
        elif position == "mid":
            self.file.drawString(x, y, text)
        elif position == "right":
            self.file.drawRightString(x, y, text)

    def random_drawing(self, fg_count: int):
        """
        This function draws random picture\n
        :param fg_count: count of figures, drawn on page
        """
        for figure in range(fg_count):
            methods = [
                self.file.bezier(randint(150, 495), randint(150, 741), randint(150, 495), randint(150, 741),
                                 randint(150, 495), randint(150, 741), randint(150, 495), randint(150, 741)),
                self.file.arc(randint(100, 495), randint(100, 741), randint(100, 495), randint(100, 741)),
                self.file.rect(randint(100, 395), randint(100, 641), randint(1, 100), randint(1, 100),
                               fill=randint(0, 1)),
                self.file.ellipse(randint(100, 495), randint(100, 741), randint(100, 495), randint(100, 741),
                                  fill=randint(0, 1)),
                self.file.circle(randint(100, 395), randint(100, 641), randint(1, 100), fill=randint(0, 1)),
                self.file.roundRect(randint(100, 395), randint(100, 641), randint(1, 100), randint(1, 100),
                                    randint(1, 100), fill=randint(0, 1))
            ]
            self.file.setFillColorRGB(uniform(0, 1), uniform(0, 1), uniform(0, 1), alpha=uniform(0, 1))
            self.file.setStrokeColorRGB(uniform(0, 1), uniform(0, 1), uniform(0, 1), alpha=uniform(0, 1))
            choice(methods)

    def draw_table(self, data: dict, x: int = 10, y: int = 10):
        """
        This function draws table from your dictionary of data\n
        size of page is 595.27,841.89\n
        :param data: dictionary with data, e.g.
        :param x, y: coordinates of left-bottom corner of table
        {
            'title': 'Table title',
            'columns': [
                {'name': 'Name', 'value': 'name'},
                {'name': 'Age', 'value': 'age'}
            ],
            'rows': [
                {'name': 'string1', 'age': 23},
                {'name': 'string2', 'age': 43}
            ]
        }
        """
        self._normal_color()
        data = self._format_data(data)
        table = Table(data=data,
                      style=[("GRID", (0, 1), (-1, -1), 1, "Black"),
                             ("FONT", (0, 0), (-1, -1), "Calibri", self.font_size),
                             ("BOX", (0, 0), (-1, -1), 1, "Black")])
        table.wrapOn(self.file, 10, 10)
        table.drawOn(self.file, x, y)

    def insert_image(self, path: str, x: int = 100, y: int = 200, width: int = None, height: int = None):
        """
        This function inserts image in pdf-file\n
        size of page is 595.27,841.89\n
        :param path: path to image
        :param x, y: coordinates of left-bottom corner of image
        :param width, height: sizes of image
        """
        image = Image(path, width, height)
        image.drawOn(self.file, x, y)

    def next_page(self):
        """
        This function turns the page\n
        """
        self._normal_color()
        self.file.drawString(565, 30, str(self.page))
        self.page += 1
        self.file.showPage()

    def save(self, author: str = 'pdf_gen', title: str = 'GENERATED'):
        """
        This function saves our file\n
        :param author: author of file
        :param title: title of file
        """
        self._normal_color()
        self.file.drawString(565, 30, str(self.page))
        self.file.setAuthor(author)
        self.file.setTitle(title)
        self.file.save()


def merge_pdf(source_paths: list, result_path: str, source_del: bool = False):
    """
    This function merges some files into one\n
    You can create some pages via "pdf" class and merge it into one pdf-file\n
    :param source_paths: paths to source files, e.g. ['c:/files/file1.pdf', 'c:/files/file2.pdf']
    :param result_path: path to result file
    :param source_del: if it`s True, function deletes source files, else not
    """
    merger = PdfFileMerger()
    opened = []
    for path in source_paths:
        file = open(path, 'rb')
        merger.append(fileobj=file)
        opened.append(file)
    result = open(result_path, 'wb')
    merger.write(result)
    result.close()
    for file in opened:
        file.close()
    if source_del:
        for path in source_paths:
            os.remove(path)
