"""
    Created on 2012-02-04
    @author: jldupont
"""
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


print greet("male", "Dupont")
"Hello M. Dupont!"

print greet("female", "Corriveau")
"Hello Mrs. Corriveau!"
