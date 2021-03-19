import setuptools
import pdf_gen

with open('Readme.md') as fr:
    long_description = fr.read()

setuptools.setup(
    name='pdf_gen',
    version=pdf_gen.__version__,
    author='Desyatnikov I.S.',
    author_email='ncab_03@mail.ru',
    description='Pdf-file generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vanya2535/pdf_gen',
    packages=setuptools.find_packages(),
    install_requires='reportlab >= 3.5.65',
    test_suite='tests',
    python_requires='>=3.7',
    platforms=["any"]
)
