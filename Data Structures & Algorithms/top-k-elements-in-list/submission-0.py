class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        return [num for num, count in sorted_items[:k]]









        
        