class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l < r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += (p+k-1)//k

            if hours <= h:
                r = k
            else:
                l = k + 1

        return l