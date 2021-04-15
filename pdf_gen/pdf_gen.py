from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.platypus import Table
from random import uniform, randint, choice


class pdf:
    def __init__(self, path: str):
        """
        Create a pdf-file object\n
        :param path: path to create file
        """
        if path[len(path) - 1] != '/' and ".pdf" not in path:
            path += '/'
        elif ".pdf" in path:
            path = path[0:path.rfind('/') + 1:1]
        path += "generated.pdf"
        self.file = Canvas(path)
        self.set_font(12)

    def set_font(self, font_size: int):
        """
        This function set up font and his size in file\n
        :param font_size: size of font
        """
        self.font_size = font_size
        using_font = ttfonts.TTFont("Calibri", "Calibri.ttf")
        pdfmetrics.registerFont(using_font)
        self.file.setFont("Calibri", self.font_size)

    def write_text(self, text: str, position: str = "mid", x: float = 297.635, y: float = 815.89):
        """"
        This function write text on defined position\n
        size of page is 595.27,841.89
        :param text: string of text to writing
        :param position: left/mid/right position of string of text
        :param x, y: coordinates of string
        """
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

    def draw_table(self, data: dict):
        """
        This function draws table from your list of dictionaries with data\n
        :param data: dictionary with data, e.g.
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
        format_data = [[data['title']]]
        add_list = []
        value_list = []
        for column_elem in data['columns']:
            add_list.append(column_elem['name'])
            value_list.append(column_elem['value'])
        format_data.append(add_list.copy())
        add_list.clear()
        for row_elem in data['rows']:
            for value in value_list:
                add_list.append(row_elem[value])
            format_data.append(add_list.copy())
            add_list.clear()
        table = Table(data=format_data,
                      style=[("GRID", (0, 1), (-1, -1), 1, "Black"),
                             ("FONT", (0, 0), (-1, -1), "Calibri", self.font_size),
                             ("BOX", (0, 0), (-1, -1), 1, "Black")])
        table.wrapOn(self.file, 10, 10)
        table.drawOn(self.file, 10, 10)

    def save(self, author: str = 'pdf_gen', title: str = 'GENERATED'):
        """
        This function saves our file\n
        :param author: author of file
        :param title: title of file
        """
        self.file.setAuthor(author)
        self.file.setTitle(title)
        self.file.save()
