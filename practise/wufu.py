from functools import reduce

def get_number(arr):
    min = len(arr)
    for i in range(len(arr[0])):
        result = reduce(lambda x, y: x+y, [int(j.strip()[i]) for j in arr.split(",")])
        if result < min:
            min = result

    return min


import numpy as np

def get_number(arr):
    ele = [list(i.strip()) for i in arr.split(",")]
    array = np.array(ele, dtype=np.int32)
    print(array)
    return np.min(np.sum(array, axis=0))


a = '111111, 000111, 111000'
print(get_number(a))
