import io
import os

from setuptools import setup


def get_version(package):
    with open(os.path.join(package, '__init__.py')) as file:
        ver_line = list(filter(lambda l: l.startswith('VERSION'), file))[0]
        ver_tuple = eval(ver_line.split('=')[-1])
    
    return '.'.join(map(str, ver_tuple))


def get_long_description(package):
    with open('README.md') as file:
        long_description = file.read()
    
    return long_description.strip()


description = 'Shameless bootleg copy of flask-mongoengine for API Star.'
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
packages = [
    'apistar_mongoengine',
]
install_requires = [
    'mongoengine>=0.15.0',
    'apistar>=0.5.12',
]
tests_require = [
    'pytest>=3.5.1',
    'flake8>=3.5.0',
    'tox>=3.0.0',
]
setup_requires = [
    'pytest-runner',
],


options = {
    'name': 'apistar-mongoengine',
    'version': get_version('apistar_mongoengine'),
    'url': 'http://github.com/njncalub/apistar-mongoengine',
    'description': description,
    'long_description': get_long_description('apistar_mongoengine'),
    'author': 'Nap Joseph Calub',
    'author_email': 'njncalub+apistar_mongoengine@gmail.com',
    'license': 'MIT',
    'packages': packages,
    'install_requires': install_requires,
    'include_package_data': True,
    'classifiers': classifiers,
    'platforms': 'any',
    'zip_safe': False,
    'tests_require': tests_require,
    'setup_requires': setup_requires,
}

setup(**options)
