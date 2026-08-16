class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for r in matrix:
            for n in r:
                arr.append(n)
        
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False