from .algorithm import Algorithm 


class InsertionSort(Algorithm): 

    def __init__(self, dataset):
        """Initialize the variable that controls the outer loop for the Insertion Sort algorithm."""

        super().__init__(dataset)
        self.j = 1

    def nextStep(self): 
        """Completes a single step in the Insertion Sort algorithm."""

        key = self.dataset[self.j]
        i = self.j - 1
        while i >= 0 and self.dataset[i] > key:
            self.dataset[i + 1] = self.dataset[i]
            self.dataset[i] = key
            i -= 1
        self.dataset[i + 1] = key

        self.j += 1