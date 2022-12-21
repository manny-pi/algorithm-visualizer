from __algorithms.bubble_sort import BubbleSort
from __algorithms.insertion_sort import InsertionSort
from __algorithms.merge_sort import MergeSort
from __algorithms.selection_sort import SelectionSort
from __renderer import Renderer
from __encoder import Encoder


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
        self.encodedDataset = Encoder.encodeDataset(self.__dataset, by="color")

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

    def sortSpeed(self, speed): 
        """Determines the speed at which the dataset is sorted.

        Sort speed choices are 'low', 'medium', 'high'
        """
        frameRate = 0
        if speed == 'low': 
            frameRate = 10
        elif speed == 'medium': 
            frameRate = 50
        elif speed == 'high': 
            frameRate = 0
        
        Renderer.setFrameRate(frameRate)


    def start(self): 
        """Starts the visualizer."""

        self.__renderer = Renderer(self)    # instantiate the Renderer object

    def cont(self): 
        """Continues the process by completed the next step in the algorithm."""

        if not self.__algorithm.finished(): 
            self.__algorithm.nextStep()


if __name__ == '__main__': 
    from random import randint as r
    proc = Processor()
    
    data = [r(1, 100) for i in range(500)]
    proc.setDataset(data)
    proc.setAlgorithm(algorithm="insertion_sort")
    proc.sortSpeed("medium")
    proc.start()
