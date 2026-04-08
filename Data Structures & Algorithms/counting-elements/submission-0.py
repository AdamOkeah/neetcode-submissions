class Solution:
    def countElements(self, arr: List[int]) -> int:
        exists_map = Counter(arr)

        count = 0
        for num in arr:
            if num + 1 in exists_map.keys():
                count += 1
        return count

        