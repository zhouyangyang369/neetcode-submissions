class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for t in range(len(temperatures)):
            if not stack:
                stack.append(0)
            
            while stack and temperatures[stack[-1]] < temperatures[t]:
                res[stack[-1]] = t - stack[-1]
                stack.pop()
            
            stack.append(t)

        return res