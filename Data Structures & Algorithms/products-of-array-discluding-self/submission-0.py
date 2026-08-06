class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            prefix = prefix * nums[i]
            res.append(prefix)
        
        for j in range(len(nums)-1, -1, -1):
            if j+1 == len(nums):
                res[j] = res[j-1] * 1
            elif (j-1) < 0:
                postfix = postfix * nums[j+1]
                res[j] = 1 * postfix
            else:
                postfix = postfix * nums[j+1]
                res[j] = res[j-1] * postfix
            
        return res
