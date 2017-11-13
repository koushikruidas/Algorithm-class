def Bsearch(self, arr, start, end):
    n = len(arr)
    mid = (end + start) // 2
    x = arr[mid]
    if x <= arr[(mid - 1 + n) % n] and x <= arr[(mid + 1) % n]:
        return arr[mid]
    elif x <= arr[n - 1]:
        return self.Bsearch(arr, start, mid - 1)
    else:
        return self.Bsearch(arr, mid + 1, end)

a = [4, 5, 6, 7, 0, 1, 2]
print(Bsearch(a, 0, len(a)-1))