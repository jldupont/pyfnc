"""
    Created on 2012-02-03
    @author: jldupont
"""
import types
import functools

def coroutine(func):
    """
    Decorator used for coroutine declaration
    """
    @functools.wraps(func)
    def start(*args, **kwargs):
        cr=func(*args, **kwargs)
        cr.next()
        return cr
    return start

def partial(fn, *pargs):
    """
    Partial Function builder
    >>> f=lambda p1,p2: p1+p2
    >>> pf=partial(f, 66)
    >>> pf(44)
    110
    """
    def _(*args):
        plist=list(pargs)
        plist.extend(list(args))
        return fn(*plist)
    return _

def check_pair(pair):
    """ (e1, e2) --> (type|value, value)
    
    >>> check_pair((True, True))
    True
    """
    e1, e2=pair
    if e1==e2 or e1==any:
        return True
    
    if type(e1)==types.TypeType:
        if type(e2)==e1:
            return True
        
    return type(e2)==e1


def check_match_type(tuples):
    """
    >>> import types, logging
    >>> check_match_type( [(True, True), (False, False)] )
    True
    >>> check_match_type( [(int, 2), (str, "string")] )
    True
    >>> check_match_type( [(int, 2), ("ok", "ok")] )
    True
    >>> check_match_type( [(int, "string"), ("ok", "ok")] )
    False
    >>> check_match_type( [(int, "string"), ("ok", str)] )
    False
    >>> check_match_type( [(int, 2), (str, "string"), ("ok", "ok")] )
    True
    >>> check_match_type( [ (types.FunctionType, logging.getLogger) ] )
    True
    """
    if len(tuples) < 2:
        return check_pair(tuples[0])
    
    def reducer(sx, y):
        """
        1-  False *  --> False
        2a) True  True --> True
        2b) True  False --> False
        3)  True  el
        4)  el el    
        """
        ## 1
        if sx==False:
            return False
        
        ## 2
        if sx==True:
            if y==True:
                return True
            if y==False:
                return False
        
        ## 3
        if sx==True:
            return check_pair(y)
        
        ## 4
        r1=check_pair(sx)
        r2=check_pair(y)
        return r1 and r2
        
    
    return reduce(reducer, tuples)

def check_arity(liste):
    """
    Verify if all the elements of liste
    have the same arity
    
    >>> check_arity( [(1,2)] )
    True
    >>> check_arity( [(1,2), (3,4) ] )
    True
    >>> check_arity( [(1,2), (3,4), (5,6,7) ] )
    False
    >>> check_arity( [('f1_p0', ('ok', 'str')), ('f1_p1', ('int', 'int')), ('f1_p2', ('int', 'str'))] )
    True
    >>> check_arity( "allo!" )
    True
    >>> check_arity( "allo" )
    True
    >>> check_arity( 666 )
    False
    """
    try: 
        if len(liste) < 2:
            return True
    except:
        return False
    
    lref=len(liste[0])
    
    def reducer(sx,y):
        """
        el    el  --> l
        True  el  -->
        False *   --> False
        """
        try:
            if sx==False:
                return False
            
            if sx==True:
                return lref==len(y)
            
            return len(sx)==lref and len(y)==lref
        except:
            return False
    
    return reduce(reducer, liste)

    
class meta_enhancer(type):
    """
    Metaclass which enhances a given set of class methods with a "return self" statement
    """
    def __new__(cls, future_class_name, 
                future_class_parents, future_class_attr):

        parent=future_class_parents[0]

        for m in future_class_attr["to_enhance"]:
            method=getattr(parent, m)

            def close_on_wrapper(method_name, method):
                def wrapper(this, *p):
                    method(this, *p)
                    return this
                return wrapper
            
            future_class_attr[m]=close_on_wrapper(m, method)
            
        return type(future_class_name, future_class_parents, future_class_attr)


    
if __name__ == '__main__':
    import doctest
    doctest.testmod()