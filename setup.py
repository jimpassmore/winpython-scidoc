# -*- coding: utf-8 -*-
"""Scientific Python libraries documentation"""

from distutils.core import setup
import os
import os.path as osp

def get_data_files(dirname):
    """Return data files in directory *dirname*"""
    flist = []
    for dirpath, _dirnames, filenames in os.walk(dirname):
        for fname in filenames:
            flist.append(osp.join(dirpath, fname))
    return flist

setup(name='Scidoc', version='1.8.1',
      description='Scidoc installs scientific libraries documentation',
      long_description="""Scidoc installs scientific libraries documentation 
(NumPy, SciPy, Matplotlib and others) in sys.prefix\Doc directory on Windows. 
Scidoc version is indexed to NumPy version.""",
      data_files=[(r'Doc', get_data_files('doc'))],
      author = "Pierre Raybaut",
      author_email = 'pierre.raybaut@gmail.com',
      maintainer = 'Jim Passmore',
      maintaner_email = 'tkd4jim@gmail.com'
      url = 'http://code.google.com/p/winpython/',
      classifiers=['Operating System :: Microsoft :: Windows'])
