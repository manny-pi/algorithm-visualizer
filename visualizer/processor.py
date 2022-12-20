from __algorithms.bubble_sort import BubbleSort
from __algorithms.insertion_sort import InsertionSort
from __algorithms.merge_sort import MergeSort
from __algorithms.selection_sort import SelectionSort
from renderer import Renderer


class Processor: 
    """Processor class. 

    This class is the entry point for the client. At the moment, we will 
    consider this to be our application code.  
    """
    
    def __init__(self): 

        self.__algorithm = None        # the user-specified sorting algorithm
        self.__dataset = None          # dataset to be sorted and visualized
        self.encodedDataset = None     # color-coded dataset that's passed to the algorithm
        self.__renderer = None         # Renderer object to draw visualization to GUI

    def setDataset(self, dataset): 
        """Stores the raw values of the dataset being sorted."""
        
        if dataset == None or dataset == []: 
            raise TypeError("Type Error: dataset cannot be null. \
                Please use the {Processor}.setDataset() function.")

        self.__dataset = list(dataset)  # deep-copy the dataset
        self.encodedDataset = self.__encodeDataset(self.__dataset)

    def setAlgorithm(self, algorithm="insertion_sort"): 
        """Select the algorithm to use for sorting. Default: Insertion Sort."""

        alg = None
        if algorithm == "bubble_sort": 
            alg = BubbleSort
        elif algorithm == "insertion_sort": 
            alg = InsertionSort
        elif algorithm == "merge_sort": 
            alg = MergeSort
        elif algorithm == "selection_sort": 
            alg = SelectionSort
        self.__algorithm = alg(self.encodedDataset) 

    def start(self): 
        """Starts the visualizer."""

        self.__renderer = Renderer(self)    # instantiate the Renderer object

    def __encodeDataset(self, dataset):
        """Color codes the values in the dataset. Uses the ReLU function to 
        convert the raw value into a hexadecimal that is then converted into RGB"""

        ret = []
        for value in dataset:
            ret.append(ColorCoded(value, (
                round((1/3)*value, 2), 
                round((2/3)*value), 
                value)))
        
        return ret

    def cont(self): 
        """Continues the process by completed the next step in the algorithm."""

        if not self.__algorithm.finished(): 
            self.__algorithm.nextStep()


class ColorCoded: 
    """Represents the components that are used for the visualization."""

    def __init__(self, value, color): 

        self.value = value
        self.color = color

    def __repr__(self): 

        return f"({self.value}, (R={self.color[0]}, G={self.color[1]}, B={self.color[2]}))"

    def __le__(self, other): 

        return self.value <= other.value
    
    def __ge__(self, other): 

        return self.value >= other.value

    def __lt__(self, other): 

        return self.value < other.value

    def __gt__(self, other): 
        
        return self.value > other.value


if __name__ == '__main__': 
    from random import randint as r
    proc = Processor()
    
    data = [r(1, 100) for i in range(10)]
    proc.setDataset(data)
    proc.setAlgorithm(algorithm="selection_sort")
    proc.start()

