class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dicts, dictt = {}, {}

        for i in range(len(s)):
            dicts[s[i]] = 1 + dicts.get(s[i], 0)
            dictt[t[i]] = 1 + dictt.get(t[i], 0)

        for key in dicts:
            if dicts[key] != dictt.get(key, 0):
                return False
        
        return True