from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):                  # Provide template for the class definition
    """Our own version of collections.Sequence abstract base class.""" 

    @abstractmethod
    def __len__(self): 
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j): 
        """Return the element at index j of the sequence.""" 
    
    def __contains__(self, val): 
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):                  # relies on __len__ method being implemented 
            if self[j] == val: 
                return True 
        return False

    def index(self, val): 
        """Return index of the first instance of val in the sequence (or raise ValueError)."""
        for j in range(len(self)): 
            if self[j] == val:                      # match found
                return j; 
        raise ValueError('value not in sequence')   # match not found
    
    def count(self, val): 
        """Return the number of elements equal to give value."""
        k = 0
        for j in range(len(self)): 
            if self[j] == val:                      # found a match 
                k += 1
        return k
