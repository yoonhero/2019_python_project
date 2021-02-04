import itertools, math

counter = 0
solution = []

def pathcounter(gridSize):
    path = []
    counter = 0
    for i in range(0, gridSize):
        path.append(0)
        path.append(1)

    print(path)
    for i in itertools.permutations(path, gridSize*2):
        if i not in solution:
            print(i)
            solution.append(i)
            counter += 1
    return counter

def pathCounter(gridSize):
    p = math.factorial (gridSize*2) / (math.factorial (gridSize)**2)
    return p

n = pathCounter(20)
print(n)