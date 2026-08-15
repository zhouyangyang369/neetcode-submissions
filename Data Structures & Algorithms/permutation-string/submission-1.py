class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        l = 0
        matches = 0
        window = {}
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            if s2[r] in need and window[s2[r]] == need[s2[r]]:
                matches += 1

            if (r-l+1) > len(s1):
                if s2[l] in need and window[s2[l]] == need[s2[l]]:
                    matches -= 1

                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                
                l += 1
            
            if matches == len(need):
                return True

        return False