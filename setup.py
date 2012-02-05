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
========

Functional style 'list' and 'dict' classes & decorators for pattern matching function dispatch. 

For more information, visit http://www.systemical.com/doc/opensource/pyfnc


Examples
========

Dictionary class 'dic' with 'return self' functionality:

        >>> d=dic({"k2":"v2"})
        >>> dr=d.update({"k1":"v1"})
        >>> self.assertEqual(d, dr)

List class 'liste' with 'return self' functionality and integrated 'map', 'reduce' and 'filter' functions:

        >>> l=liste()
        >>> lr=l.extend([1,2,3])
        >>> self.assertEqual(len(l), 3)
        >>> self.assertEqual(l, lr)
        
        >>> f=lambda x:x+10
        
        >>> lm=l.map(f)
        >>> self.assertEqual(lm, [11, 12, 13])
        >>> self.assertEqual(l, [11, 12, 13])


Erlang style function dispatch:

    >>> @pattern('male', str)
    ... def greet_male(p1, p2):
    ...     return "Hello M. %s!" % p2

    >>> @pattern('female', str)
    ... def greet_female(p1, p2):
    ...        return "Hello Mrs. %s!" % p2

    >>> @patterned
    ... def greet(p1, p2):
    ...    pass

    >>> print greet("male", "Dupont")
    "Hello M. Dupont!"

    >>> print greet("female", "Corriveau")
    "Hello Mrs. Corriveau!"


Tests
=====

Tests can be performed using `nosetests` in the root directory.
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
