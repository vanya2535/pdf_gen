import unittest
import os
from pdf_gen.pdf_gen import pdf


def pathCheck(path: str):
    path = pdf._get_path(pdf, path)
    if path.count(':') == 1:
        if path.count('<>?"\*') == 0:
            return True


def fileCompare(example_path: str, compare_path: str):
    ext = 0
    with open(example_path, 'rb') as example, open(compare_path, 'rb') as compare:
        ex = (string for string in example)
        cmp = (string for string in compare)
        for string in ex:
            if string != next(cmp):
                ext += 1
                if ext > 2:
                    return False
        else:
            return True


class pdfTest(unittest.TestCase):

    def test_get_path(self):
        paths = ['c:/path', 'c::/path', 'C:/path/pdf.p\df', 'c:/path/pd>f.pdf.pdf.gen', 'c: /path/ ']
        names = ['gen', 'generated', 'gena', 'gener', 'fic']
        for path in paths:
            for name in names:
                self.assertTrue(pathCheck(path))
                self.assertEqual(pdf._get_path(pdf, path, name), f'c:/path/{name}.pdf')

    def test_format_data(self):
        data1 = {
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
        ndata1 = [
            ['Table title'],
            ['Name', 'Age'],
            ['string1', 23],
            ['string2', 43]
        ]
        data2 = {
            'title': 'Table title',
            'columns': [
                {'name': 'Name', 'value': 'name'},
                {'name': 'Lastname', 'value': 'lastname'},
                {'name': 'Age', 'value': 'age'}
            ],
            'rows': [
                {'name': 'string1', 'lastname': '1st', 'age': 23},
                {'name': 'string2', 'lastname': '2nd', 'age': 43},
                {'name': 'string3', 'lastname': '3rd', 'age': 35}
            ]
        }
        ndata2 = [
            ['Table title'],
            ['Name', 'Lastname', 'Age'],
            ['string1', '1st', 23],
            ['string2', '2nd', 43],
            ['string3', '3rd', 35]
        ]
        data = [data1, data2]
        ndata = [ndata1, ndata2]
        for id in range(2):
            self.assertEqual(pdf._format_data(pdf, data[id]), ndata[id])

    def test_pdfCreate(self):
        paths = ['c:/projects/pdf_generator/path', 'c::/projects/pdf_generator/path',
                 'C:/projects/pdf_generator/path/pdf.p\df', 'c:/projects/pdf_generator/path/pd>f.pdf.pdf.gen',
                 'c: /projects/pdf_generator/path/ ']
        names = ['gen', 'generated', 'gena', 'gener', 'fic']
        for path in paths:
            for name in names:
                testing = pdf(path, name)
                testing.save()
                self.assertTrue(os.path.exists(testing._get_path(path, name)))
                os.remove(testing._get_path(path, name))

    def test_table_text(self):
        file = pdf('c:/projects/pdf_generator/tests', 'compare')
        file.write_text('Testing file', 'right', 350, 800)
        data = {
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
        file.draw_table(data)
        file.save()
        self.assertTrue(fileCompare('c:/projects/pdf_generator/tests/compare.pdf',
                                    'c:/projects/pdf_generator/tests/test.pdf'))
