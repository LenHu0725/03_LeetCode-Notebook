"""
名称：Python八大排序法
作者：Hoo
说明：直接插入排序、希尔排序、简单选择排序、堆排序、归并排序、基数排序
Copyright：https://www.cnblogs.com/woider/p/6835466.html
"""

#######################################################
#               直接排序(插入排序)                     #
#######################################################
# 时间复杂度:O(n^2)    空间复杂度:O(1)    稳定性：稳定   #
def insert_sort(array):
    
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    
    return array


#######################################################
#               希尔排序(插入排序)                     #
#######################################################
# 时间复杂度:O(n)   空间复杂度:O(n√n)    稳定性：不稳定  #
def shell_sort(array):
    gap = len(array)
    
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    
    return array


#######################################################
#               简单选择排序(选择排序)                  #
#######################################################
# 时间复杂度:O(n^2)   空间复杂度:O(1)    稳定性：不稳定  #
def select_sort(array):
    for i in range(len(array)):
        x = i # 最小index
        for j in range(i, len(array)):
            if array[j] < array[x]:
                x = j
        array[i], array[x] = array[x], array[i]

    return array


#######################################################
#                     堆排序                          #
#######################################################
# 时间复杂度:O(nlog2n)  空间复杂度:O(1)  稳定性：不稳定  #
def heap_sort(array):
    def heap_adjust(parent):
        child = 2 * parent + 1  # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1  # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = \
                heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, array = array.copy(), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        array.insert(0, heap.pop())
        heap_adjust(0)
    return array


#######################################################
#                     冒泡排序                         #
#######################################################
# 时间复杂度:O(n^2)    空间复杂度:O(1)    稳定性：稳定  #
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


#######################################################
#                     快速排序                         #
#######################################################
#时间复杂度:O(nlog2n) 空间复杂度:O(nlog2n) 稳定性：不稳定#
def quick_sort(array):
    def recursive(begin, end):
        if begin > end:
            return
        l, r = begin, end
        pivot = array[l]
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l - 1)
        recursive(r + 1, end)

    recursive(0, len(array) - 1)
    return array


#######################################################
#                     归并排序                         #
#######################################################
# 时间复杂度:O(nlog2n)    空间复杂度:O(1)   稳定性：稳定 #
def merge_sort(array):
    def merge_arr(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) != 0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)

    return recursive(array)


#######################################################
#                     基数排序                         #
#######################################################
# 时间复杂度:O(d(r+n)) 空间复杂度:O(rd+n)   稳定性：稳定 #
def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array