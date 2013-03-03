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


@pattern("ok", any)
def wtest_ok(_1, _2):
    return "ok"

@pattern("error", str)
def wtest_nok(_1, _2):
    return "error"

@patterned
def wtest(code, msg): pass

class TestCases(unittest.TestCase):

    def test_0(self):
        self.assertEqual(wtest("ok", "some string"), "ok")
    
        
     
if __name__ == '__main__':
    unittest.main()

        