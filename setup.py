import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='myshowsscrobbler',
    version='0.1.0',

    author='Andrew Lineyschikov',
    author_email='andrew.lineyshikov@gmail.com',

    url='https://github.com/Elcaten/myshowsscrobbler',
    description='scrobbler for myshows.me',
    long_description=read('README.md'),

    license='GPL',
    packages=['myshowsscrobbler'],
    install_requires=[
        'myshows',
        'requests'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: End Users/Desktop'
    ],
    keywords=['myshows', 'scrobbler'],
)