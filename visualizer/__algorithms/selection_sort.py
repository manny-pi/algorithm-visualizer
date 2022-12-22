from .algorithm import Algorithm


class SelectionSort(Algorithm): 

    def __init__(self, dataset): 
        """Initialize the variable that controls the outer loop for the Selection Sort algorithm.."""

        super().__init__(dataset)
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