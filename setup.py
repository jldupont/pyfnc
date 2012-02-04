#!/usr/bin/env python
"""
    Jean-Lou Dupont's pyfnc
    
    Created on 2012-01-19
    @author: jldupont
"""
__author__  ="Jean-Lou Dupont"
__version__ ="0.1.0"


from distutils.core import setup
from setuptools import find_packages

DESC="""
Overview
--------

Python decorators for pattern matching function dispatch

"""

setup(name=         'pyfnc',
      version=      __version__,
      description=  'Python decorators for pattern matching function dispatch',
      author=       __author__,
      author_email= 'jl@jldupont.com',
      url=          'http://www.systemical.com/doc/opensource/pyfnc',
      package_dir=  {'': "src",},
      packages=     find_packages("src"),
      scripts=      [
                     ],
      package_data = {
                      '':[ "*.gif", "*.png", "*.jpg" ],
                      },
      include_package_data=True,                      
      zip_safe=False
      ,long_description=DESC
      )
