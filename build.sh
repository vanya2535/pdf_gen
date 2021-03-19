python setup.py sdist
python setup.py bdist_wheel
python setup.py build
twine upload dist/*