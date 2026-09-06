# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.prev = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if curr.val <= self.prev:
                return False
            
            self.prev = curr.val

            curr = curr.right

        return True