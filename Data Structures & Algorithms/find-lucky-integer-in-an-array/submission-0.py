class Solution:
    def findLucky(self, arr: List[int]) -> int:

        freq_map = Counter(arr)

        answer = -1

        for k,v in freq_map.items():
            if k == v and k > answer:
                answer = k
        
        return answer
        