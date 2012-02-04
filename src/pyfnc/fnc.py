"""
    pyfnc
    
    @author: Jean-Lou Dupont
    
"""
from functools import wraps
from fnc_tools import check_match_type, check_arity

MDICT={}

def patterned(f):
    """
    Use this decorator on the last function of the pattern
    """
    global MDICT
    ### speed-up execution:
    ###  provide this dict to the wrapper closure
    psf=MDICT.get((f.__module__, f.__name__), {})
    
    @wraps(f)
    def wrapper(*pa):
        """
        Time to perform pattern matching
        
        psf: list of (fname, sig)        
        """
        for fn, sig in psf:
            zliste=zip(sig, pa)
            if check_match_type(zliste):
                return fn(*pa)
        
        sig=map(type, pa)
        raise RuntimeError("No matching function '%s' with sig: %s" % (f.__name__, str(sig)))
    ##############
    return wrapper


class pattern(object):
    """
    Use this decorator on each function of the pattern
    """
    def __init__(self, *ps):
        self.ps=ps
        
    def basename(self, f):
        bits=f.split(".")
        fname=bits[-1]
        return fname.split("_")[0]
        
    def __call__(self, f):
        """
        Time to add the signature to globals
        as it needs to be done before the 'base function' is called
        """
        global MDICT
        
        base_function_name=self.basename(f.__name__)
        
        psb=MDICT.get((f.__module__, base_function_name), [])
        psb.append((f, self.ps))
        MDICT[(f.__module__, base_function_name)]=psb
    
        ### check that all functions of the pattern 
        ### have the same arity
        check=check_arity(psb)
        if not check:
            raise RuntimeError("Wrong arity for function '%s'" % f.__name__)
    
        @wraps(f) 
        def wrapped_f(*pa):
            return f(*pa)
    
        return wrapped_f


if __name__=="__main__":
    import doctest
    doctest.testmod()
