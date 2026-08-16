class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i, each in enumerate(nums):
            if each in diff_dict:
                return [diff_dict[each], i]
            diff_dict[target - each] = i