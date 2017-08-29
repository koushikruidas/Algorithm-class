def counting_sort(array):
    n = len(array)
    k = 15
    l = [0]*k

    for x in range(n):
        l[array[x]] += 1

    for i in range(k):
        if l[i] != 0:
            for x in range (l[i]):
                print(i)

def counting_sort_ex(array):
    n = len(array)
    k = 15
    l = []
    for i in range(k):
        l.append([])

    o = []
    for i in range(n):
        l[array[i]].append(array[i])
    print(l)

    for x in range(k):
        o.extend(l[x])
    print(o)


array = [5,3,6,2,1,8,12,6]
# counting_sort(array)
counting_sort_ex(array)