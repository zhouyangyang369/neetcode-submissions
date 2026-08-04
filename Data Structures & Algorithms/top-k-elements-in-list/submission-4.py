class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        bucket = [[] for _ in range(len(nums) +1)]

        for key, v in hashmap.items():
            bucket[v].append(key)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result
