class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_map = Counter(nums)

        for x in freq_map.values():
            if x % 2 != 0:
                return False
        
        return True