"""
    Created on 2012-02-03
    @author: jldupont
"""
import logging
import unittest
import operator

try:
    from pyfnc import liste
except:
    import os, sys
    ap=os.path.abspath(__file__)
    dn=os.path.dirname
    base=dn(dn(dn(ap)))
    sys.path.insert(0, base)
    from pyfnc import liste



class TestCases(unittest.TestCase):
    
    def test_extend(self):
        l=liste()
        lr=l.extend([1,2,3])
        self.assertEqual(l, lr)

    def test_insert(self):
        l=liste()
        l.extend([1,2,3])
        self.assertEqual(len(l), 3)
        lr=l.insert(1, 4)
        self.assertEqual(lr, [1,4,2,3])


    def test_push(self):
        l=liste()
        l.extend([1,2,3])
        self.assertEqual(len(l), 3)
        lr=l.push(0)
        self.assertEqual(lr, [0,1,2,3])

        
    def test_map(self):
        l=liste()
        l.extend([1,2,3])
        self.assertEqual(len(l), 3)
        
        f=lambda x:x+10
        
        lr=l.map(f)
        self.assertEqual(lr, [11, 12, 13])
        self.assertEqual(l, [11, 12, 13])
        
    def test_all(self):
        l=liste()
        l.extend([True, True, True])
        
        r=l.all(operator.truth)
        self.assertTrue(r)

    def test_any(self):
        l=liste()
        l.extend([True, False, True])
        
        r=l.any(operator.truth)
        self.assertTrue(r)
        
    def test_filter(self):
        l=liste()
        l.extend([0,1,2,3,4,5,6,7,8,9])
        
        f=lambda x:x % 2==0
        
        lr=l.filter(f)
        self.assertEqual([0,2,4,6,8], lr)

    def test_reduce(self):
        l=liste()
        l.extend([1,2,3,4,5,6,7,8,9])
        
        f=lambda x, y: x * y
        self.assertEqual(25, f(5, 5))
        
        r=l.reduce(f)
        self.assertEqual(9*8*7*6*5*4*3*2*1, r)
     
    def test_slice(self):
        l=liste()
        l.extend([1,2,3,4,5,6,7,8,9])

        sl=l[-1]
        self.assertEqual(9, sl)
        self.assertEqual(len(l), 9)
        
    def test_slice2(self):
        l=liste()
        l.extend([1,2,3,4,5,6,7,8,9])

        sl=l[0:2]
        self.assertEqual(sl, [1,2])
        self.assertEqual(len(l), 9)
     
if __name__ == '__main__':
    unittest.main()

        