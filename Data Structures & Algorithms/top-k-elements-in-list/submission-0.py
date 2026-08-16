class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ_dict = {}
        for each in nums:
            occ_dict[each] = occ_dict.get(each, 0) + 1
        
        # Creating a list for each possible occurence
        bucket = [[] for _ in range(len(nums)+1)]

        for num, count in occ_dict.items():
            bucket[count].append(num)
        
        output = []
        for x in (range(len(nums), -1, -1)):
            if len(bucket[x]) != 0:
                for y in bucket[x]:
                    output.append(y)
                    if len(output) == k:
                        return output
            
            