import numpy as np

def is_sorted(array):
    increasing = True
    decreasing = True
    for i in range(len(array)-1):
        if array[i] - array[i+1] > 3 or array[i] - array[i+1] < 1:
            increasing = False
        if array[i] - array[i+1] < -3 or array[i] - array[i+1] > -1:
            decreasing = False
    return increasing or decreasing

def can_be_sorted(array):
    for i in range(len(array)):
        aux = np.delete(array, i)
        if is_sorted(aux):
            return True
    return False

with open("day2/input.txt", "r") as input:
    
    score = 0

    for line in input:
        array = np.array(line.split(), dtype=int)

        if is_sorted(array) or can_be_sorted(array):
            score += 1

    print(score)

            

        

        
        
            

        
