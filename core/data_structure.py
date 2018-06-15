# -*- coding: utf-8 -*-

"""A data contianer of kmol editor."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import Dict, Hashable


class DataDict:
    
    """A wrapper class contain the data of nodes."""
    
    def __init__(self, data: Dict[Hashable, str] = {}):
        self.__data = {}
        self.__data.update(data)
        self.__saved = {key: True for key in data}
    
    def clear(self):
        """Clear data."""
        self.__data.clear()
        self.__saved.clear()
    
    def __getitem__(self, key: Hashable) -> str:
        """Get item string."""
        if key in self.__data:
            return self.__data[key]
        else:
            return ""
    
    def __setitem__(self, key: Hashable, context: str):
        """Set item."""
        self.__data[key] = context
        self.__saved[key] = False
    
    def __delitem__(self, key: Hashable):
        """Delete the key and avoid raise error."""
        if key in self.__data:
            del self.__data[key]
            del self.__saved[key]
    
    def is_saved(self, key: Hashable) -> bool:
        """Return saved status."""
        return self.__saved[key]
    
    def saveAll(self):
        """Change all saved status."""
        for key in self.__data:
            self.__saved[key] = True
    
    def newNum(self) -> int:
        """Get a unused number."""
        i = 0
        while i in self.__data:
            i += 1
        else:
            return i
