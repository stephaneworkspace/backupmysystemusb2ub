"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import os
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


def read_requirements():
    """Requirements pip"""
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name='backupmysytemusb2usb',
    version='0.0.11',
    install_requires=(read_requirements()),
    description='Backup a usb key to another usb key with the same space disk',
    long_description=(read('README.rst') + '\n\n'),
    url='https://github.com/stephaneworkspace/backupmysystemusb2usb.git',
    author='Stéphane Bressani',
    author_email='s.bressani@bluewin.ch',
    license='GPLv3+',
    packages=find_packages(include=['backupmystemusb2usb',
                                    'backupmystemusb2usb.*']),
    python_requires='>=3.7',
    zip_safe=False,
    classifiers=[
        'Development Status :: 0 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Disk tool',
    ],
)
