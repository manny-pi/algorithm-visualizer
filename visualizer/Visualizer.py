"""

"""

import __algorithms.BubbleSort as BubbleSort
import __algorithms.InsertionSort as InsertionSort
import __algorithms.MergeSort as MergeSort
import __algorithms.SelectionSort as SelectionSort


class Visualizer: 

    def __init__(): 
        self.__dataset = None          # dataset to be sorted and visualized
        self.encodedDataset = None     # color-coded dataset to be passed into the algorithm
        self.__algorithm = None        # the algorithm being used to sort

    def setDataset(self, dataset): 
        """Stores the raw values of the dataset being sorted."""
        
        self.__dataset = list(dataset)
        self.__encodedDataset = self.__encodeDataset(self.__dataset)

    def setAlgorithm(self, algorithm="insertion_sort"): 
        """Select the algorithm to use for sorting. Default is Insertion Sort."""

        if algorithm == "bubble_sort": 
            self.__algorithm = BubbleSort(self.__encodedDataset)
        elif algorithm == "insertion_sort": 
            self.__algorithm = InsertionSort(self.__encodedDataset)
        elif algorithm == "merge_sort": 
            self.__algorithm = MergeSort(self.__encodedDataset)
        elif algorithm == "selection_sort": 
            self.__algorithm = SelectionSort(self.__encodedDataset)


    def start(self): 
        """Starts the visualizers."""

        self.__render()

    def __encodeDataset(self): 
        """Color codes the values in the dataset."""

        if self.__dataset == None or self.__dataset == []: 
            raise TypeError("Type Error: dataset cannot be null. Please use the {Visualizer}.setDataset() function")

    def __render(self): 
        """Renders the color-coded dataset to the screen"""

        pass 


class ColorCoded: 
    """Represents the components that are used for the visualization"""

    def __init__(self, value, color): 
        self.value = value
        self.color = color
