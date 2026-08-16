class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for each in s:
            freq[each] = freq.get(each, 0) + 1
        
        for each in t:
            if freq.get(each, 0) <= 0:
                return False
            freq[each] -= 1
        
        return True
