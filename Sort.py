import random
import numpy as np

# 冒泡排序
def bubble(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, n - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 选择排序
def select(arr):
    n = len(arr)
    for i in range(0, n-1):
        minidx = i
        for j in range(i+1, n):
            if arr[j] < arr[minidx]:
                minidx = j
        if minidx != i:
            arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr

# 插入排序
def insert(arr):
    n = len(arr)
    for i in range(n):
        preidx = i - 1
        cur = arr[i]
        while cur < arr[preidx] and preidx >= 0:
            arr[preidx + 1] = arr[preidx]
            preidx -= 1
        arr[preidx + 1] = cur
    return arr

# 希尔排序
def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            current = arr[i]
            preidx = i - gap
            while current <= arr[preidx] and preidx >= 0:
                arr[preidx+gap] = arr[preidx]
                preidx -= gap
            arr[preidx+gap] = current
        gap = int(gap / 2)
    return arr

# 归并排序
def mergeSort(arr):
    if len(arr) > 1:
        middle = int(len(arr) / 2)
        left = mergeSort(arr[:middle])
        right = mergeSort(arr[middle:])
        i, j = 0, 0
        temp = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
        if i == len(left):
            for k in right[j:]:
                temp.append(k)
        else:
            for k in left[i:]:
                temp.append(k)
        return temp
    return arr

# 快速排序
def quickSort(arr, left, right):
    low = left
    high = right
    if left < right:
        # 一趟快排
        base = arr[left]
        while left < right:
            while left < right and arr[right] >= base:
                right -= 1
            arr[left], arr[right] = arr[right], arr[left]
            while left < right and arr[left] <= base:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        quickSort(arr, low, left-1)
        quickSort(arr, right+1, high)
    return arr


if __name__ == '__main__':
    data = np.random.randint(2, 50, 20)
    print('原始数据：  ', data)
    print('bubleSort:  ', bubble(data))
    print('selectSort: ', select(data))
    print('insertSort: ', insert(data))
    print('shellSort:  ', shellSort(data))
    print('mergeSort:  ', np.array(mergeSort(data)))
    print('quickSort:  ', quickSort(data, 0, len(data)-1))