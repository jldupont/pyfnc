'''
Created on Feb 7, 2012

@author: jldupont
'''
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


@pattern(False, False)
def checktransition_nopf(previous, current):
    return ("nop", current)

@pattern(False, True)
def checktransition_up(previous, current):
    return ("tr", "up")

@pattern(True, True)
def checktransition_nopt(previous, current):
    return ("nop", current)

@pattern(True, False)
def checktransition_down(previous, current):
    return ("tr", "down")

@pattern(None, True)
def checktransition_nt(previous, current):
    return ("tr", "up")

@pattern(None, False)
def checktransition_nf(previous, current):
    return ("tr", "down")

@pattern(type, type)
def checktransition_xy(x,y):
    return ("nop", None)

@patterned
def checktransition(previous, current):
    pass

ct=checktransition

class TestCases(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(ct(False, False), ('nop', False))

    def test_2(self):
        self.assertEqual(ct(True, True), ('nop', True))


     
if __name__ == '__main__':
    unittest.main()
