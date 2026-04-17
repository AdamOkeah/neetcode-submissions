class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        freq_map = Counter(arr)

        distinct_arr = []

        for key in freq_map:
            if freq_map[key] == 1:
                distinct_arr.append(key)


        if len(distinct_arr) == 0 or k > len(distinct_arr):
            return ""
        else:
            return distinct_arr[k-1]


        