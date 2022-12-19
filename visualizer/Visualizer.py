"""

"""

from __algorithms.bubble_sort import BubbleSort
from __algorithms.insertion_sort import InsertionSort
from __algorithms.merge_sort import MergeSort
from __algorithms.selection_sort import SelectionSort


class Visualizer: 

    def __init__(self): 

        self.__dataset = None          # dataset to be sorted and visualized
        self.encodedDataset = None     # color-coded dataset to be passed into the algorithm
        self.__algorithm = None        # the algorithm being used to sort

    def setDataset(self, dataset): 
        """Stores the raw values of the dataset being sorted."""
        
        if dataset == None or dataset == []: 
            raise TypeError("Type Error: dataset cannot be null. Please use the {Visualizer}.setDataset() function.")

        self.__dataset = list(dataset)  # deep-copy the dataset
        self.encodedDataset = self.__encodeDataset(self.__dataset)

    def setAlgorithm(self, algorithm="insertion_sort"): 
        """Select the algorithm to use for sorting. Default is Insertion Sort."""

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
        """Starts the visualizers."""

        self.__render() 

    def __encodeDataset(self, dataset): 
        """Color codes the values in the dataset."""

        ret = []
        for value in dataset:
            ret.append(ColorCoded(value, ((1/3)*value, (2/3)*value, value)))
        
        return ret

    def __render(self): 
        """Renders the color-coded dataset to the screen."""

        while not self.__algorithm.finished(): 
            self.__algorithm.nextStep()


class ColorCoded: 
    """Represents the components that are used for the visualization."""

    def __init__(self, value, color): 

        self.value = value
        self.color = color

    def __repr__(self): 

        return f"({self.value}, {self.color})"

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
    viz = Visualizer()
    
    data = [r(1, 100) for i in range(10)]
    viz.setDataset(data)
    viz.setAlgorithm(algorithm="selection_sort")
    viz.start()
