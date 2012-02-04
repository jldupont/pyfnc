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


@pattern('ok', int)
def tfnc_KI(p1, p2):
    return ("KI", p1, p2)

@pattern(int, str)
def tfnc_IS(p1, p2):
    return ('IS', p1, p2)

@pattern(int, int)
def tfnc_II(p1, p2):
    return ('II', p1, p2)

@pattern(list, list)
def tfnc_LL(p1, p2):
    return ("LL", p1, p2)

@pattern(str, types.FunctionType)
def tfnc_SF(p1,p2):
    return ("SF", p1, p2)

@pattern(list, dict)
def tfnc_LD(p1, p2):
    return ("LD", p1, p2)

@pattern(bool, bool)
def tfnc_BB(p1, p2):
    return ("BB", p1, p2)

@pattern(any, any)
def tfnc_AA(p1, p2):
    return ('AA', p1, p2)

@patterned
def tfnc(p1, p2):
    pass


class TestCases(unittest.TestCase):
    
    def test_II(self):
        self.assertEqual(('II', 1, 2), tfnc(1,2))

    def test_KI(self):
        self.assertEqual(('KI', 'ok', 2), tfnc('ok',2))

    def test_IS(self):
        self.assertEqual(('IS', 666, "string"), tfnc(666, "string"))

    def test_LL(self):
        self.assertEqual(('LL', [1,2], [3,4]), tfnc([1,2], [3,4]))

    def test_SF(self):
        self.assertEqual(('SF', "ok", logging.getLogger), tfnc("ok", logging.getLogger))

    def test_LD(self):
        l=[1,2,3,4]
        d={"k1": "v1", "k2":"v2"}
        self.assertEqual(("LD", l, d), tfnc(l, d))

    def test_BB1(self):
        self.assertEqual( ("BB", True, False), tfnc(True, False))

    def test_BB2(self):
        self.assertEqual( ("AA", "error", False), tfnc("error", False))

    def test_AA1(self):
        self.assertEqual(('AA', {}, {}), tfnc({}, {}))

    def test_AA2(self):
        self.assertEqual(('AA', (), ()), tfnc((), ()))

     
if __name__ == '__main__':
    unittest.main()

        