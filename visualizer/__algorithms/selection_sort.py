from . import algorithm


class SelectionSort(algorithm.Algorithm): 
    def __init__(self, encodedDataset): 
        """Initialize the outer variable for the selection sort method."""
        
        self.encodedDataset = encodedDataset
        self.j = 0

    def nextStep(self): 
        """Completes a single step in the Selection Sort algorithm."""

        smallest = self.encodedDataset[self.j].value
        indexOfSmallest = self.j
        i = self.j + 1
        while i < len(self.encodedDataset):
            if self.encodedDataset[i].value < smallest.value:
                smallest = self.encodedDataset[i]
                indexOfSmallest = i
            i += 1

        current = self.encodedDataset[self.j]
        self.encodedDataset[self.j] = smallest
        self.encodedDataset[indexOfSmallest] = current
        self.j += 1

        print(self.encodedDataset)

    def finished(self):
        """Check if the dataset is sorted. 
        
        Return True if the dataset is sorted. 
        Return False if the dataset is not sorted."""

        for i in range(len(self.encodedDataset) - 1): 
            a = self.encodedDataset[i]
            b = self.encodedDataset[i+1]
            if not a <= b: 
                return False
        return True