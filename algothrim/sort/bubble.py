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


def quick_sort(nums):
    base = nums[0]


def select_sort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums
        

a = [2, 4, 6, 88, 1, 7, 20, 13]
print(buddle_sort(a[:]))
print(insert_sort(a[:]))
print(select_sort(a[:]))
print(a)
