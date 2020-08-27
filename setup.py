# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marvin']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.3.1,<4.0.0', 'ply>=3.11,<4.0', 'seaborn>=0.10.1,<0.11.0']

setup_kwargs = {
    'name': 'marvin',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'repl.it user',
    'author_email': 'replituser@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
