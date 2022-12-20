class SelectionSort: 
    def __init__(self, dataset): 
        """Initialize the outer variable for the selection sort method."""
        
        self.dataset = dataset
        self.j = 0

    def nextStep(self): 
        """Completes a single step in the Selection Sort algorithm."""

        smallest = self.dataset[self.j]
        indexOfSmallest = self.j
        i = self.j + 1
        while i < len(self.dataset):
            if self.dataset[i] < smallest:
                smallest = self.dataset[i]
                indexOfSmallest = i
            i += 1

        current = self.dataset[self.j]
        self.dataset[self.j] = smallest
        self.dataset[indexOfSmallest] = current
        self.j += 1

    def finished(self):
        """Check if the dataset is sorted. 
        
        Return True if the dataset is sorted. 
        Return False if the dataset is not sorted."""

        for i in range(len(self.dataset) - 1): 
            a = self.dataset[i].value
            b = self.dataset[i+1].value
            if not a <= b: 
                return False
        return True
