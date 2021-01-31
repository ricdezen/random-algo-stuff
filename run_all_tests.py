import os

from setuptools import find_packages

if __name__ == '__main__':
    for package in find_packages():
        if '.test' in package:
            continue
        os.system(f'cmd /c "python -m pytest -s {package}/test"')
