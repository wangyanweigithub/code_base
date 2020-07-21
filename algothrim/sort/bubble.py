def buddle_sort(nums):
    for i in range(len(nums) - 1):
        j = 0
        while j < len(nums) - i - 1:
            if nums[j] > nums[j+1]: 
                nums[j], nums[j+1] = nums[j+1], nums[j]
            j = j + 1
    return nums


def insert_sort(nums):
    k, j = 0, 1
    for i in range(1, len(nums)):
        j = i
        while j >= 1:
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            j = j - 1

    return nums


def quick_process(nums, low, heigh):
    i, j = low, heigh
    while i < j:
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            break
        else:
            j = j - 1

    while i < j:
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            j = j - 1
            break
        else:
            i = i + 1

    if i > 1:
        quick_process(nums, 0, i-1)

    if i < heigh - 1:
        quick_process(nums, i+1, heigh)

    return nums

def select_sort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums
        

def heap_sort(nums):
    def make_heap(nums):
        for i in reversed(range(len(nums)//2)):
            insert_heap(nums, i, len(nums))

        return nums

    def insert_heap(nums, j, length):
        while 2*j + 1 < length:
            if 2*j + 2 >= length:
                min_index = 2*j + 1
            else:
                min_index = 2*j+1 if nums[2*j+1] < nums[2*j+2] else 2*j+2
            if nums[j] <= nums[min_index]:
                break
            nums[j], nums[min_index] = nums[min_index], nums[j]
            j = min_index

    make_heap(nums)
    for i in reversed(range(1, len(nums))):
        nums[i], nums[0] = nums[0], nums[i]
        insert_heap(nums, 0, i)

    nums.reverse()
    return nums

a = [2, 4, 6, 88, 1, 7, 20, 13]
print(buddle_sort(a[:]))
print(insert_sort(a[:]))
print(select_sort(a[:]))
print(heap_sort(a[:]))
print(quick_process(a[:], 0, len(a)-1))
print(a)
