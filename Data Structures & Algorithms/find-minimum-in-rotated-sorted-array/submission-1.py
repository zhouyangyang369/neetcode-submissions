class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = nums[0]
        last = nums[-1]

        if first <= last:
            return first
        
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r)//2
            if nums[mid] < first:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
                else:
                    r = mid - 1
            else:
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                else:
                    l = mid + 1