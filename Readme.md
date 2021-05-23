# Pdf_gen guide

## Installing
pip3 install pdf_gen

## How to use
```python
from pdf_gen.pdf_gen import pdf

my_file = pdf(path, name) # path - path to your file, name - name of file
my_file.random_drawing(count) # count - count of drawings
my_file.set_font(size) # size - size of font
data = {
            'title': 'Table title',
            'columns': [
                {'name': 'X_name', 'value': 'x'},
                {'name': 'Y_name', 'value': 'y'}
            ],
            'rows': [
                {'x': 10, 'y': 20},
                {'x': 5, 'y': 10}
            ]
}
my_file.draw_table(data) # data - dict with data
my_file.write_text() # text - string of text to writing, position - left/mid/right position of string of text, 
#x and y - coordinates of string
my_file.save(author, title) # author - author of file, title - title of file
```
## Example
```python
from pdf_gen.pdf_gen import pdf

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
file.random_drawing(10)
file.save() 
```
## You can create some pdf and merge it into one
```python
from pdf_gen.pdf_gen import pdf, merge_pdf

file_names = ['first', 'second', 'third', 'fourth']
paths = []
for file_name in file_names:
    page = pdf('/files/', f'{file_name}.pdf')
    paths.append(f'/files/{file_name}.pdf')
    page.write_text(file_name)
    page.random_drawing(10)
    page.save()
merge_pdf(paths, '/files/res.pdf', True)
```