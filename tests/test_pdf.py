import unittest
import os
from pdf_gen.pdf_gen import pdf


def pathCheck(path: str):
    path = pdf._get_path(pdf, path)
    if path.count(':') == 1:
        if path.count('<>?"\*') == 0:
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
        paths = ['c:/path', 'c::/path', 'C:/path/pdf.p\df', 'c:/path/pd>f.pdf.pdf.gen', 'c: /path/ ']
        for path in paths:
            testing = pdf(path)
            testing.save()
            path = pdf._get_path(pdf, path)
            self.assertTrue(os.path.exists(path))
            os.remove(path)
