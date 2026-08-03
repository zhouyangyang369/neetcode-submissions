class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # key [0] * 26, value [group sublist]
        
        for m in strs:
            key  = [0] * 26
            for n in m:
                key[ord(n) - ord('a')] += 1
            hashmap[tuple(key)].append(m)

        return list(hashmap.values())