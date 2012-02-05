"""
    Enhanced list

    Created on 2012-02-04
    @author: jldupont
"""
from fnc_tools import partial, meta_enhancer


class liste(list):
    """
    Enhanced list
    """

    to_enhance=['append', 'extend', 'insert', 'remove', 'reverse', 'sort']
    __metaclass__=meta_enhancer

    def __init__(self, *p):
        list.__init__(self, *p)

        self.last_value=None

    def __setitem__(self, *p):
        list.__setitem__(self, *p)
        return self        

    def push(self, el):
        """
        Pushes an element at the front of the list
        
        Replaces the usual list.insert(0, el)
        """
        list.insert(self, 0, el)
        return self
    
    def clone(self):
        return liste(self)
    
    def do(self, f, *args, **kwargs):
        """
        Calls 'f' on self, returns result
        """
        return partial(f, *args, **kwargs)(self)
    
    def tee(self, f, *args, **kwargs):
        """
        Calls 'f' on self, returns self, keeps 'last value'
        """
        self.last_value=partial(f, *args, **kwargs)(self)
        return self

    def invoke(self, function_name, *args, **kwargs):
        """
        Invokes 'function_name(*args, **kwargs)' on each element
        
        List([1,2]).invoke('__str__')
        <=>
        List([1,2]).map(lambda x: x.__str__())
        """
        return self.map(lambda x: getattr(x, function_name)(*args, **kwargs))

    def find(self, f, *args, **kwargs):
        """
        Returns the first element matching the predicate 'f' else returns None
        """
        _f=partial(f, *args, **kwargs)
        
        for el in self:
            if _f(el):
                return el
        
    def count(self, f, *args, **kwargs):
        """
        Counts elements in the list matching 'f' predicate
        """
        _f=partial(f, *args, **kwargs)
        
        count=0
        for el in self:
            if _f(el):
                count=count+1
        return count
        

    def attr(self, attr):
        """
        Retrieves a specific attribute from all objects
        
        List([obj]).attr('attr')
        <=>
        List([obj]).map(lambda x: x.attr)
        """
        return self.map(lambda x: getattr(x, attr))

    def all(self, f, *args, **kwargs):
        """
        Applies 'f' to all elements and expects 'True' for all results
        """
        _f=partial(f, *args, **kwargs)

        for el in self:
            if not _f(el):
                return False

        return True

    def any(self, f, *args, **kwargs):
        """
        Applies 'f' to all elements and expects at least 1 'True' result
        """
        _f=partial(f, *args, **kwargs)

        for el in self:
            if _f(el):
                return True

        return False

    def map(self, f, *args, **kwargs):
        """
        Applies 'f' to all elements
        
        returns 'self'
        """
        _f=partial(f, *args, **kwargs)
        
        self[:]=map(_f, self)
        return self

    def filter(self, f, *args, **kwargs):
        """
        Keeps only the elements where f(el)==True
        """
        _f=partial(f, *args, **kwargs)
        
        self[:]=filter(_f, self)
        return self
    
    def reduce(self, f, *args, **kwargs):
        """
        Reduce
        """
        _f=partial(f, *args, **kwargs)
        return reduce(_f, self)

    def __getslice__(self, *args, **kwargs):
        return liste(list.__getslice__(self, *args, **kwargs))

