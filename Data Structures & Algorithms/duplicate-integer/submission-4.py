class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        duplicate = False
        for value in freq_map.values():
            if value > 1:
                duplicate = True
            
        return duplicate