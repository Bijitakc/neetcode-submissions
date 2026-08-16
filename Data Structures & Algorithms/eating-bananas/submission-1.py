import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        least_k = right

        while left <= right:
            mid = (left + right) // 2
            hour = 0
            for each in piles:
                hour = hour + math.ceil(each/mid)
            if hour > h:
                left = mid + 1
            if hour <= h:
                right = mid - 1
                least_k = min(least_k, mid)

        return least_k
            
            
