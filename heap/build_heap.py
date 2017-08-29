def build_heap(array):
    n = len(array) -1
    for i in range((n//2),-1,-1):
        heapify(array,i,n)
    return array

def heapify(array, i , n):
    left = 2*i +1
    right = 2*i +2
    if(n >= right and array[right] > array[left] and array[right] > array[i]):
        swap(array,right,i)
        heapify(array,right,n)
    elif(n >= left and array[left] > array[i]):
        swap(array,left,i)
        heapify(array,left,n)

def swap(arr1,x,y):
    t = arr1[x]
    arr1[x] = arr1[y]
    arr1[y] = t
    return arr1

def dlt(array):
    ar = []
    n = len(array) - 1
    swap(array,0,n)
    ar = array.pop()
    heapify(array,0,(len(array)-1))
    return ar

def heap_sort(array):
    n = len(array)
    sorted_array = []
    for i in range (n):
        sorted_array.append(dlt(array))
    return sorted_array

arr = [1,2,3,4,5,0,9,6]

heap = build_heap(arr)
print("max heap :")
print(heap)

deleted_element = dlt(arr)
print("deleted element : ")
print(deleted_element)

print(heap)

arraySort = heap_sort(arr)
print("sorted array :")
print(arraySort)

