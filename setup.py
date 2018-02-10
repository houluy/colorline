from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='colorline',
    version='1.0.2',
    description='Colorful output in command line',
    url='https://github.com/houluy/colorline',
    author='Houlu',
    author_email='houlu8674@bupt.edu.cn',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='color',
    packages=['colorline',],
    python_requires='>=3',
    test_suite='nose.collector',
    tests_require=['nose'],
)
