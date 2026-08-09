class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ''
        longest = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in string:
                string = string + s[r]
                r += 1
            else:
                if len(string) > longest:
                    longest = len(string)
                l = string.find(s[r])
                l += 1
                string = string[l:r]
        if len(string) > longest:
            longest = len(string)
        return longest