class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        sorted_map = OrderedDict(sorted(freq_map.items(), reverse = True))

        for key, value in sorted_map.items():
            if value == 1:
                return key
        return -1       

            
        