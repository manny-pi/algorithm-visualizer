def findMax(data): 
    """Return the maximum element from the nonempty Python list."""
    biggest = data[0]
    for val in data: 
        if val > biggest: 
            biggest = val
    return biggest

from random import randint
from time import time 
def analyzePerformance(algorithm, data=None, size=10, min=1, max=1000, steps=100): 
    """Runs the specified algorithm on a randomly generated dataset, and returns metrics on its performance. 

    algorithm: callable
    min:       the minimum value in the dataset
    max:       the maximum value in the dataset
    steps 
    """
    if not isinstance(min, int): 
        ValueError("'min' must be of type Integer")
    elif not isinstance(max, int): 
        ValueError("'max' must be of type Integer")
    elif not isinstance(steps, int): 
        ValueError("'steps' must be of type Integer")

    inputSizes = range(1, 100001, 1000) # Input sizes we want to test 
    executionData = {}                  # Store the runtimes and average runtime for each input size
    epochs = 10
    for size in inputSizes: 
        runtimes = [] 
        for run in range(epochs):       # Run the algorithm for the given input size n times
            # Generate the dataset 
            data = [randint(10, 100) for i in range(size)] 
            # Run and time the algorithm, then store the results
            startTime = time()
            findMax(data)
            endTime = time()
            runtimes.append(round(endTime - startTime, 7)) 
        executionData[size] = {"Runtimes": runtimes, "Average": round(sum(runtimes)/len(runtimes), 7)}

    print(executionData.keys())
    for inputSize in executionData.keys(): 
        print("n=%s: %r" % (inputSize, executionData[inputSize]))

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(50, 50))

if __name__ == '__main__':
    analyzePerformance(findMax)
