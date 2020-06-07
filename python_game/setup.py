try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': "My Project",
    'author': 'Edward Harley',
    'url': None,
    'author_email': 'test@test.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['game'],
    'scripts': [],
    'name': 'game'
}

setup(**config)