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


def bubble_up(array, index):
    if index//2 == 0:
        return
    if array[index - 1] > array[(index//2) - 1]:
        swap(array, array[index - 1],array[(index//2) - 1])
        bubble_up(array, index//2)


def insert(array, key):
    n = len(array)
    if n == 0:
        array.append(key)
    else:
        array.append(key)
        bubble_up(array,len(array))


class PriorityQueue:
    """Array-based priority queue implementation."""

    def __init__(self):
        """Initially empty priority queue."""
        self.queue = []

    def __len__(self):
        # Number of elements in the queue.
        return len(self.queue)

    def append(self, key):
        """Inserts an element in the priority queue."""
        if key is None:
            raise ValueError('Cannot insert None in the queue')
        PriorityQueue.insert(self.queue, key)

    def min(self):
        """The smallest element in the queue."""
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def pop(self):
        """Removes the minimum element in the queue.

        Returns:
            The value of the removed element.
        """
        if len(self.queue) == 0:
            return None
        return PriorityQueue.dlt(self.queue)

    @staticmethod
    def build_heap(array):
        n = len(array) - 1
        for i in range((n // 2), -1, -1):
            PriorityQueue.heapify(array, i, n)
        return array

    @staticmethod
    def heapify(array, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        if (n >= right and array[right] < array[left] and array[right] < array[i]):
            PriorityQueue.swap(array, right, i)
            PriorityQueue.heapify(array, right, n)
        elif (n >= left and array[left] < array[i]):
            PriorityQueue.swap(array, left, i)
            PriorityQueue.heapify(array, left, n)

    @staticmethod
    def swap(arr1, x, y):
        t = arr1[x]
        arr1[x] = arr1[y]
        arr1[y] = t
        return arr1

    @staticmethod
    def dlt(array):
        n = len(array) - 1
        PriorityQueue.swap(array, 0, n)
        ar = array.pop()
        PriorityQueue.heapify(array, 0, (len(array) - 1))
        return ar

    @staticmethod
    def bubble_up(array, index):
        if index // 2 == 0:
            return
        if array[index - 1] < array[(index // 2) - 1]:
            PriorityQueue.swap(array, index - 1, index // 2 - 1)
            PriorityQueue.bubble_up(array, index // 2)

    @staticmethod
    def insert(array, key):
        n = len(array)
        if n == 0:
            array.append(key)
        else:
            array.append(key)
            PriorityQueue.bubble_up(array, len(array))


arr = [1,2,3,4,5,0,9,6]

#
# pq = PriorityQueue()
# for i in range(len(arr)):
#     pq.append(arr[i])
#
# for i in range(len(arr)):
#     print(pq.pop())
#
heap = build_heap(arr)
print("max heap :")
print(heap)

# deleted_element = dlt(arr)
# print("deleted element : ")
# print(deleted_element)
#
# print(heap)
#
# arraySort = heap_sort(arr)
# print("sorted array :")
# print(arraySort)

