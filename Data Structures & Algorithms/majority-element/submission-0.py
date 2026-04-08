class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        freq_map = Counter(nums)

        for key, value in freq_map.items():
            if freq_map[key] > n / 2:
                return key
        