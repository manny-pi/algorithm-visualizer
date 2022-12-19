class Progression:
    """Iterator producing a generic progression. 

    Default iterator produces the whole number 0, 1, 2, ...
    """

    def __init__(self, start=0): 
        """Initialize current to the first value of the progression.""" 
        self._current = start 

    def _advance(self):
        """Update self._current to a new a value. 

        This should be overriden by a subclass to customize progression. 

        By convention, if current is set to None, this designates the 
        end of a finite progression.
        """ 
        self._current += 1

    def __next__(self): 
        """Return the next element, or else raise StopIteration error.""" 
        if self._current is None:       # our convention value to return
            raise StopIteration()
        else: 
            answer = self._current      # record current value to return
            self._advance()             # advance to prepare for next time
            return answer               # return the answer 
    
    def __iter__(self): 
        """By convention, an iterator must return itself as an iterator."""
        return self 

    def print_progression(self, n): 
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):               
    """Iterator producing an arithmetic progression.""" 

    def __init__(self, start=0, increment=1): 
        """Create a new arithmetic progression.

        increment       the fiexed constant to add to each term (default 1)
        start           the first term of the progression (default 0)
        """
        super().__init__(start)             # initialize base class 
        self.__increment = increment
    
    def _advance(self):                     # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self.__increment   


class GeometricProgression(Progression): 
    """Iterator producing a geometric progression."""

    def __init__(self, start=1, base=2): 
        """Create a new geometric progression.
        
        start       the first term of the progression (default 1)
        base        the fixed constant multiplied to each term (default 2) 
        """
        super().__init__(start)
        self._base = base 

    def _advance(self): 
        """Update current value by multiplying it by the base value."""
        self._current *= self._base 


class FibonacciProgression(Progression): 
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1): 
        """Create a new fibonacci progress

        first       the first term of the progression (default 0)
        second      the second term of the progression (default 1)
        """
        super().__init__(first)         # start progression at first 
        self._prev = second - first     # fictitious value preceding the first
        
    def _advance(self): 
        """Update current value bhy taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    print('Default progression:') 
    Progression().print_progression(10)
    
    print('Arithmetic progression with increment 5:') 
    ArithmeticProgression(5).print_progression(10)
    
    print('Arithmetic progression with increment 5 and start 2:')
    ArithmeticProgression(5, 2).print_progression(10)
   
    print('Geometric progression with default base:') 
    GeometricProgression().print_progression(10)
   
    print('Geometric progression with base 3:') 
    GeometricProgression(3).print_progression(10)
  
    print('Fibonacci progression with default start values:') 
    FibonacciProgression().print_progression(10)
 
    print('Fibonacci progression with start values 4 and 6:') 
    FibonacciProgression(4, 6).print_progression(10)