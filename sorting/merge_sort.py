def merge(left,right):
    arr = []
    i = 0
    j = 0
    length_left = len(left)
    length_right = len(right)
    while length_left > i and length_right > j:
        if left[i] > right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    while j < length_right:
        arr.append(right[j])
        j += 1
    while i < length_left:
        arr.append(left[i])
        i += 1
    return arr

def merge_sort(array):
    n = len(array)
    if n == 1:
        return array
    else:
        left = merge_sort(array[0 : n//2])
        right = merge_sort(array[n//2 : n])
        return merge(left, right)



# left = [17, 14, 13, 10, 9]
# right = [ 8, 6, 5, 3]
# me = merge(right,left)
# print(me)

array = [10,12,18,1,9,10]
sort = merge_sort(array)
print(sort)