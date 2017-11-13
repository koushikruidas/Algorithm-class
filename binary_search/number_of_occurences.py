class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        initial_index = Solution.Bsearch(A, 0, len(A) - 1, B)
        count = 1
        i = initial_index + 1
        j = initial_index - 1
        if initial_index is not None:
            while A[i] == B:
                count += 1
                i += 1
            while A[j] == B:
                count += 1
                j -= 1
        else:
            return 0

    @staticmethod
    def Bsearch(arr, start, end, n):
        if start == end:
            if arr[start] == n:
                return start
            else:
                return None

        mid = (end + start) // 2
        x = arr[mid]
        if x < n:
            return Solution.Bsearch(arr, mid + 1, end, n)
        else:
            return Solution.Bsearch(arr, start, mid, n)


