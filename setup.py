import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    version='0.1.0',
    name='myshowsscrobbler',
    description='VLC scrobbler for myshows.me',
    long_description=read('README.md'),
    url='TODO: github url',
    download_url='TODO: download url',
    author='Andrew Lineyschikov',
    author_email='andrew.lineyshikov@gmail.com',
    license='MIT',
    packages=['myshowsscrobbler'],
    install_requires=[
        'oauthlib',
        'requests_oauthlib',
        'myshowsapi',
        'appdirs'
    ],
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords=['myshows', 'vlc', 'scrobbler'],
)