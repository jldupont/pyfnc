"""
    Created on 2012-02-03
    @author: jldupont
"""
import logging
import types
import unittest

try:
    from pyfnc import patterned, pattern
except:
    import os, sys
    ap=os.path.abspath(__file__)
    dn=os.path.dirname
    base=dn(dn(dn(ap)))
    sys.path.insert(0, base)
    from pyfnc import patterned, pattern


@pattern('male', str)
def greet_male(p1, p2):
    return "Hello M. %s!" % p2

@pattern('female', str)
def greet_female(p1, p2):
    return "Hello Mrs. %s!" % p2

@patterned
def greet(p1, p2):
    pass


class TestCases(unittest.TestCase):
    
    def test_male(self):
        self.assertEqual("Hello M. Smith!", greet('male', 'Smith'))

    def test_female(self):
        self.assertEqual("Hello Mrs. Adam!", greet('female', 'Adam'))

     
if __name__ == '__main__':
    unittest.main()

        