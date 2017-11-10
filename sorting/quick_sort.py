def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p,r):
        if arr[j] < x:
            i +=1
            swap(arr,i,j)
    swap(arr, i+1,r)
    return i+1


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q+1, r)


def median_find(arr, p, r, i):
    q = partition(arr, p, r)
    if i == q:
        return arr[q]
    elif i < q:
        return median_find(arr, p, q - 1, i)
    else:
        return median_find(arr, q+1, r, i)


Arr = [1, 4, 2, 6, 3, 48, 9, 0, 11, -25]
print(median_find(Arr, 0, 9, ))
