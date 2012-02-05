"""
    Created on 2012-02-03
    @author: jldupont
"""
import unittest

try:
    from pyfnc import dic
except:
    import os, sys
    ap=os.path.abspath(__file__)
    dn=os.path.dirname
    base=dn(dn(dn(ap)))
    sys.path.insert(0, base)
    from pyfnc import dic



class TestCases(unittest.TestCase):
    
    def test_update(self):
        d=dic()
        dr=d.update({"k1":"v1"})
        self.assertEqual(d, dr)

    def test_clear(self):
        d=dic()
        d.update({"k1":"v1"})
        self.assertEqual(len(d), 1)
        dr=d.clear()
        self.assertEqual(len(dr), 0)
        self.assertEqual(dr, d)
        
    def test_all(self):
        
        def starts_kv(k,v):
            return k[0]=="k" and v[0]=="v"
        
        d=dic()
        d.update({"k1":"v1", "k2": "v2"})
        
        self.assertTrue(d.all(starts_kv))
        
    def test_any(self):
        
        def starts_kv(k,v):
            return k[0]=="k" and v[0]=="v"

        d=dic()
        d.update({"a1":"a1", "k2": "v2"})
        self.assertTrue(d.any(starts_kv))

    def test_safe(self):
        d=dic()
        d.safe(True)
        
        self.assertEqual(d[0], None)
        
    def test_each(self):
        d=dic()
        d.update({"K1":"V1", "K2":"V2"})
        
        f=lambda k,v: (k.lower(), v.lower())
        dr=d.map(f)
        self.assertEqual(dr, {"k1":"v1", "k2":"v2"})
        
    def test_do(self):
        d=dic()
        d.update({"K1":"V1", "K2":"V2"})

        dr=d.do(len)
        self.assertEqual(len(d), dr.last_value)
        
    def test_count(self):
        d=dic()
        d.update({"K1":"V1", "K2":"V2", "A1":"AV1"})
        
        predicate=lambda k,v: k.lower().startswith("k")
        
        count=d.count(predicate)
        self.assertEqual(2, count)
        
        

     
if __name__ == '__main__':
    unittest.main()

        