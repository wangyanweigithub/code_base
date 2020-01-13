def binary_search(target, item):
    low = 0
    high = len(target) - 1
    
    while low <= high:
        mid = (low + high) //  2
        if target[mid] == item:
            return mid
        if target[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 7))

