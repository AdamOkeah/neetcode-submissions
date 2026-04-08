from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = Counter(nums)


        duplicate = False
        for value in freq_map.values():
            if value > 1:
                duplicate = True
            
        return duplicate