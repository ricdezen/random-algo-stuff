'''
Simple module to generate README files for submodules.
Add a readme.json file to customize readme file with:
- title
- description
Otherwise module name and docstring are used.
'''

__author__ = "Riccardo De Zen <riccardodezen98@gmail.com>"

import importlib
import json
from setuptools import find_packages
from pkgutil import iter_modules
from pathlib import Path
from typing import Union, Set, Mapping, Iterable


class MarkdownDoc():

    def __init__(self, path: Union[Path, str]):
        '''
        Parameters:
            path : Union[Path, str]
                Path for the output file. No extension check is made, will be printed as plain text.
        '''
        if isinstance(path, str):
            path = Path(path)
        self.output_file = path
        self.content = ''

    def paragraph(self, *paragraphs: Iterable[str]):
        '''
        Add one or more paragraphs to the document's output.
        Adds an empty line after it.

        Parameters:
            paragraphs : Iterable[str]
                varargs for paragraphs to insert. Each paragraph is stripped of whitespaces and
                appended two line finishes.
        '''
        for par in paragraphs:
            self.content = self.content + "{}\n\n".format(par.strip())

    def header(self, title: str, weight: int = 1, bold: bool = False, italic: bool = False):
        '''
        Parameters:
            title : str
                The title for the header. Will be stripped of whitespaces and appended two line
                finishes. Defaults to one.

            weight : int
                Int from 1 to 6 indicating the weight of the header (html h1 to h6).

            bold : bool
                Wether the title should be bold, False by default.

            italic : bool
                Wether the title should be italic, False by default.

        Raises:
            ValueError : if weight out of range.
        '''
        if weight < 1 or weight > 6:
            raise ValueError("Weight out of range.")

        header = '#' * weight + ' '
        decoration = '{}'
        if italic:
            decoration = '*' + decoration + '*'
        if bold:
            decoration = '**' + decoration + '**'

        self.content = self.content + header + decoration.format(title.strip()) + '\n\n'

    def write(self):
        '''
        Write the file to it's output destination.
        '''
        with self.output_file.open('w+') as output:
            output.write(self.content)


def get_readme(package: str = '.') -> MarkdownDoc:
    '''
    Retrieve readme document with info for a package. Modules must not have dots in their name.

    Parameters:
        package : str
            The package for which to retrieve the readme info.

    Returns:
        A MarkdownDoc for the package using the information on the readme.json file, if present.
        Otherwise, package name and docstring are used.
    '''
    impored = importlib.import_module(package)
    package_path = package.replace('.', '/')
    config_path = Path(package_path, 'readme.json')
    document = MarkdownDoc(Path(package_path, 'README.md'))

    config = dict()
    if config_path.exists():
        with config_path.open() as config_file:
            config = json.load(config_file)

    document.header(config.get('title', module_to_header(package)), 1)
    document.paragraph(config.get('description', impored.__doc__ or ''))
    return document


def get_all_modules(path: Union[str, Path] = '.') -> Set[str]:
    '''
    Retrieve the string names of all the modules found by searching recursively from a certain
    root directory. Modules must not have dots in their name.

    Parameters:
        path : Union[str, Path]
            The path in which to begin the search.

    Returns:
        Set[str] : The Set containing the absolute names of all the packages and modules that were
        found. You can immediately import them via importlib.
    '''
    modules = set()
    for pkg in find_packages('.'):
        modules.add(pkg)
        pkgpath = Path(path, pkg.replace('.', '/'))
        for info in iter_modules([pkgpath]):
            if not info.ispkg:
                modules.add(pkg + '.' + info.name)
    return modules


def no_test_modules(modules: Set[str]) -> Set[str]:
    '''
    Parameters:
        modules : Set[str]
            The modules to filter.

    Returns:
        The modules except the ones that contain a 'test' package or module in their path.
    '''
    return {m for m in modules if "test" not in m.split('.')}


def group_modules(modules: Set[str]) -> Mapping[str, Set[str]]:
    '''
    Group the modules based on their first level parent.

    Parameters:
        modules : Set[str]
            The set of modules to group.

    Returns:
        Mapping[str, Set[str]] : The parent module mapped to its child modules.
    '''
    parents = [m for m in modules if len(m.split('.')) == 1]
    children = [m for m in modules if m not in parents]
    # All children with p as parent.
    return {p: [c for c in children if c.split('.')[0] == p] for p in parents}


def module_to_header(name: str) -> str:
    '''
    Parameters:
        name : str
            Absolute module name.

    Returns:
        Module name with capitalized initials and without _ and .
    '''
    rel_name = name.split('.')[-1]
    rel_name = rel_name.replace('_', ' ')
    return ' '.join(word.capitalize() for word in rel_name.split())


if __name__ == "__main__":

    modules = get_all_modules()
    modules = no_test_modules(modules)
    grouped = group_modules(modules)

    # Append each module's docstring.
    for package, modules in grouped.items():
        document = get_readme(package)
        for m in modules:
            imported = importlib.import_module(m)
            title = module_to_header(m)
            content = imported.__doc__ or ''
            document.header(title, 3, True)
            document.paragraph(content)
        document.write()
