class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict = {}
        if len(s) != len(t):
            return False
        
        for each in s:
            if each in count_dict:
                count_dict[each] += 1
            else:
                count_dict[each] = 1
        
        for each in t:
            if each in count_dict:
                count_dict[each] -= 1
                if count_dict[each] == 0:
                    count_dict.pop(each)
            else:
                return False
        
        return count_dict == {}