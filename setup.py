from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

def readme():
    try:
        with open(path.join(here, 'README'), encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ''

setup(
    name='torrentcheck',
    version='0.1.2',
    py_modules=['torrentcheck'],
    description='Check the integrity of torrent downloads.',
    long_description=readme(),
    url='https://github.com/clee704/torrentcheck',
    author='Choongmin Lee',
    author_email='choongmin@me.com',
    license='MIT',
    classifiers=[
        # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='torrent',
    install_requires=[
        'bencode == 1.0',
    ],
    entry_points={
        'console_scripts': [
            'torrentcheck=torrentcheck:main'
        ],
    },
)
