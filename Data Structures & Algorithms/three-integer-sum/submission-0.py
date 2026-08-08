class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_triple = nums[i] + nums[left] + nums[right]
                if sum_triple < 0:
                    left += 1
                    
                elif sum_triple > 0:
                    right -= 1
                    
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return res