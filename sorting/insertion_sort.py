def insertion(array):
    n = len(array)
    for i in range(1,n,1):
        j = i
        while j > 0 and array[j-1] < array[j]:
            swap(array, j - 1, j)
            j -= 1
    return array


def swap(array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp


arr = [14, 17, 3, 5, 8, 6, 9, 10, 13]

sort = insertion(arr)
print(sort)