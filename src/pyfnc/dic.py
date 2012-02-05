"""
    Enhanced dictionary
    
    Created on 2012-02-04
    @author: jldupont
"""
from fnc_tools import meta_enhancer

class dic(dict):
    """
    Enhanced dictionary
    """
    to_enhance=["setdefault", "clear", "update",]

    __metaclass__=meta_enhancer

    def __init__(self, safe=False):
        """
        If `safe` is True, then retrieving an undefined key will return `None` instead of throwing an exception
        """
        dict.__init__(self)
        self._safe=safe
        self._lock=False

    def lock(self, state):
        self._lock=state
        
        
    def __setitem__(self, key, value):
        if self._lock:
            return
        
        dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        if self._safe:
            return self.get(key, None)
        
        return dict.__getitem__(self, key)

    
    def _f(self, f, *args, **kwargs):
        """
        Partial Function builder
        """
        def _(x, y):
            return f(x, y, *args, **kwargs)
        return _

    def all(self, f, *args, **kwargs):
        """
        Applies 'f' to all [k:v] pairs and expects 'True' for all results
        """
        _f = self._f(f, *args, **kwargs)

        for x, y in self.items():
            if not _f(x, y):
                return False

        return True

    def any(self, f, *args, **kwargs):
        """
        Applies 'f' to all [k:v] pairs and expects at least 1 'True' result
        """
        _f = self._f(f, *args, **kwargs)

        for x, y in self.items():
            if _f(x, y):
                return True

        return False

            
    