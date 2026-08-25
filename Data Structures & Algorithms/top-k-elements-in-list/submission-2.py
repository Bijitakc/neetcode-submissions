from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        return sorted(count_dict, key=lambda x: count_dict[x], reverse=True)[:k]
