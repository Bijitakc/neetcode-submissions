class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_c = 0
        for each in set_nums:
            if (each-1) not in set_nums:
                stop = False
                t = 1
                while stop is False:
                    if (each + t) in set_nums:
                        t += 1
                    else:
                        stop = True
                max_c = max(max_c, t) 
        return max_c
