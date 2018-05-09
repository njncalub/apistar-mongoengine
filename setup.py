import io
import os

from setuptools import setup


def get_version(package):
    with open(os.path.join(package, '__init__.py')) as file:
        ver_line = list(filter(lambda l: l.startswith('VERSION'), file))[0]
        ver_tuple = eval(ver_line.split('=')[-1])
    
    return '.'.join(map(str, ver_tuple))


description = 'Shameless bootleg copy of flask-mongoengine for API Star.'
install_requires = [
    'mongoengine>=0.15.0',
    'apistar>=0.5.12',
]
packages = [
    'apistar_mongoengine',
]
classifiers = [
    'Development Status :: 1 - Planning',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

options = {
    'name': 'apistar-mongoengine',
    'version': get_version('apistar_mongoengine'),
    'url': 'http://github.com/njncalub/apistar-mongoengine',
    'description': description,
    'author': 'Nap Joseph Calub',
    'author_email': 'njncalub+apistar_mongoengine@gmail.com',
    'license': 'MIT',
    'packages': packages,
    'install_requires': install_requires,
    'include_package_data': True,
    'classifiers': classifiers,
    'platforms': 'any',
    'zip_safe': False,
}

setup(**options)
