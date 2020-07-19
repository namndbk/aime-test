import random
import time
import threading
import math


def partition(arr, left, right):
    pivot = arr[left]
    low = left + 1
    high = right
    while True:
        while low <= high and arr[high] > pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[left], arr[high] = arr[high], arr[left]
    return high


def quick_sort_normal(arr, left, right):
    if left >= right:
        return
    i = left
    j = right
    pivot = arr[(left + right) // 2]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    if left < j:
        quick_sort_normal(arr, left, j)
    if i < right:
        quick_sort_normal(arr, i, right)


def quick_sort(arr, left, right):
    if left >= right:
        return
    p = partition(arr, left, right)
    quick_sort(arr, left, p - 1)
    quick_sort(arr, p + 1, right)


def parallel_quick_sort(arr, num_threads):
    """
    :param arr: array
    :param num_threads: numbers of thread, powers of 2
    :return: None
    """
    num_divide = int(math.log2(num_threads))
    list_index = []
    left = 0
    right = len(arr) - 1
    if left >= right:
        return
    if right <= 2:
        quick_sort_normal(arr, left, right)
        return
    for i in range(num_divide):
        if i == 0:
            pivot = partition(arr, left, right)
            temp_index = [[left, pivot - 1], [pivot + 1, right]]
            list_index.append(temp_index)
        else:
            temp_index = []
            index = list_index[-1]
            for j, c in enumerate(index):
                l, r = int(c[0]), int(c[-1])
                if l >= r:
                    break
                pivot = partition(arr, l, r)
                temp_index.append([l, pivot - 1])
                temp_index.append([pivot + 1, r])
            list_index.append(temp_index)
    list_index = list_index[-1]
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=quick_sort_normal, args=(arr, list_index[i][0], list_index[i][-1], ))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    arr = [random.randint(-10000000, 10000000) for _ in range(100000000)]
    start_time = time.time()
    parallel_quick_sort(arr, 4)
    executed_time = time.time() - start_time
    print("\tTime: {}".format(executed_time))