import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012020S1P11',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description="# docassemble.P11\r\n\r\nMyDocs is an application created for Hutt St Centre for the purpose of assisting people to locate identity documentation ('ID'). Currently, there is no single website or resource which simply explains where and how to obtain essential  self-identification documents. Users of MyDocs can use the application to select the ID that they already have and the ID that they are seeking to obtain. The application will use this data to provide information which will assist the user in their ID application process. Our ultimate goal for creating MyDocs is to create an empowering tool which provides people experiencing disadvantage, who may seek Hutt St Centre's services, with the opportunity to feel a sense of connection and belonging.\r\n\r\n## Authors\r\n\r\nYianni Chapley, chap0094@flinders.edu.au\r\n\r\nOlympia Balopitos, balo0028@flinders.edu.au\r\n\r\nLaura Stephenson, step0176@flinders.edu.au\r\n",
      long_description_content_type='text/markdown',
      author='Olympia Balopitos',
      author_email='balo0028@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012020S1P11/', package='docassemble.LLAW33012020S1P11'),
     )

