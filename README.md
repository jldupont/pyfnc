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
    ... 	return "Hello M. %s!" % p2

	>>> @pattern('female', str)
	... def greet_female(p1, p2):
    ...		return "Hello Mrs. %s!" % p2

	>>> @patterned
	... def greet(p1, p2):
    ...	pass

	>>> print greet("male", "Dupont")
	"Hello M. Dupont!"

	>>> print greet("female", "Corriveau")
	"Hello Mrs. Corriveau!"


Clean looking reducers:


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
    


Tests
=====

Tests can be performed using `nosetests` in the root directory.

Installation
============

A source package is provided through the CheeseShop on http://pypi.python.org/ . 

History
=======

0.1.0 : support for function names with multiple '_'

0.1.0 : initial release 

