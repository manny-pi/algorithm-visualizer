from .algorithm import Algorithm


class MergeSort(Algorithm): 

    def __init__(self, dataset): 
        """Initialize the variable that controls the divide-and-conquer section of the Merge Sort algorithm."""

        super().__init__(dataset)
        self.width = 1
        self.n = len(self.dataset)

    def nextStep(self): 
        """Completes a single step in the Merge Sort algorithm."""

        l = 0
        while (l < self.n):
            r = min(l + (self.width * 2 - 1), self.n - 1)		
            m = min(l + self.width - 1, self.n - 1)
            self.__merge(self.dataset, l, m, r)
            l += (self.width * 2)
        self.width *= 2

    def __merge(self, a, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = a[l + i]
        for i in range(0, n2):
            R[i] = a[m + i + 1]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1
