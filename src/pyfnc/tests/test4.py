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


@pattern(False, any)
def comp_reducer_FA(p1, p2):
    return False

@pattern(str, str)
def comp_reducer_SS(p1, p2):
    if p1==p2:
        return p1
    return False

@patterned
def comp_reducer(p1, p2):
    """
    Reducer
    
    Check if all strings are equal
    """


def strings_comparator(l):
    """
    Returns the common string if all elements of 'l' are equal
    else returns False 
    """
    if len(l)<2:
        return False
    
    return reduce(comp_reducer, l)
    
sc=strings_comparator

class TestCases(unittest.TestCase):

    def test_0(self):
        l=[]
        self.assertEqual(sc(l), False)
    
    def test_1(self):
        l=["s1", ]
        self.assertEqual(sc(l), False)

    def test_2(self):
        l=["s1", "s1"]
        self.assertEqual(sc(l), "s1")

    def test_3(self):
        l=["s1", "s1", "s1"]
        self.assertEqual(sc(l), "s1")
        
    def test_4(self):
        l=["s1", "s2"]
        self.assertEqual(sc(l), False)

    def test_5(self):
        l=["s1", "s2", "s3"]
        self.assertEqual(sc(l), False)
        
    def test_6(self):
        l=[0, 1, 2]
        self.assertEqual(sc(l), False)

    def test_7(self):
        """ only strings are compared """
        l=[0, 0, 0]
        self.assertEqual(sc(l), False)
        
     
if __name__ == '__main__':
    unittest.main()

        