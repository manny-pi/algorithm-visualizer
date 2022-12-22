from .algorithm import Algorithm


class MergeSort(Algorithm): 

    def __init__(self, dataset): 
        """Initialize the variable that controls the divide-and-conquer section of the Merge Sort algorithm."""

        super().__init__(dataset)

    def nextStep(self): 
        raise NotImplementedError("{MergeSort}.nextStep() hasn't been implemented yet.")

import math
def mergeSort(_in, p, r):
    """Divides the problem into subproblems."""

    if p < r:
        q = math.floor((p + r) / 2)         # Calculate midpoint q of sub-array A[p.. r]
        mergeSort(_in, p, q)                # Call mergeSort on sub-array A[p.. q]
        mergeSort(_in, q + 1, r)            # Call mergeSort on sub-array A[q + 1.. r]
        mergeSortAux(_in, p, q, r)          # Call merge on sub-array A[p.. r]

def mergeSortAux(_in, p, q, r):
    """Sorts the values in the subproblem."""
    
    n_1 = q - p + 1     # Compute length of A[p.. q]
    n_2 = r - q         # Compute length of A[q + 1.. r]

    L = []              # New array to hold sub-array A[p.. q]
    R = []              # New array to hold sub-array A[q + 1 .. r]

    # Copy sub-array A[p.. q] to L
    for i in range(n_1):
        L.append(_in[p + i])

    # Copy sub-array A[q + 1.. r] to R 
    for j in range(n_2):
        R.append(_in[q + j + 1])

    # Add sentinel values to the arrays
    L.append(None)
    R.append(None)

    # Compare values from L and R, and sort the array
    i = 0
    j = 0
    for k in range(p, r + 1):

        # Execute if reached sentinel value on left sub-array
        if L[i] is None:
            _in[k] = R[j]
            j += 1

        # Execute if reached sentinel value on right sub-array
        elif R[j] is None:
            _in[k] = L[i]
            i += 1

        # Exe cute if not reached sentinel value
        else:
            if L[i] <= R[j]:
                _in[k] = L[i]  # Replace the element at _in[k]
                i += 1         # Move on to the next element in L

            else:
                _in[k] = R[j]
                j += 1