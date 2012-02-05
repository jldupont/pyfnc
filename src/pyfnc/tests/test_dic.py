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
        d=dic(safe=True)
        
        self.assertEqual(d[0], None)
        
    def test_set_lock(self):
        d=dic()
        d.lock(True)
        d["k1"]="v1"
        self.assertEqual( d, {} )
        d.lock(False)
        d["k1"]="v1"
        self.assertEqual( d, {"k1":"v1"} )
        

     
if __name__ == '__main__':
    unittest.main()

        