def selection(array):
    n = len(array)
    for i in range(n):
        max = i
        for j in range(i+1,n,1):
            if array[j] > array[max]:
                max = j
        swap(array, i, max)
    return array

def swap(array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

ar = [14, 17, 3, 5, 8, 6, 9, 10, 13]
hi = selection(ar)
print(hi)