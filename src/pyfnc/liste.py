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

    def push(self, el):
        """
        Pushes an element at the front of the list
        
        Replaces the usual list.insert(0, el)
        """
        list.insert(self, 0, el)
        return self
    
    def _f(self, f, *args, **kwargs):
        """
        Partial Function builder
        """
        def _(x):
            return f(x, *args, **kwargs)
        return _

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
