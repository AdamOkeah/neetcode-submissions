class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for x in range(len(arr)):
            if x == len(arr)-1:
                arr[x] = -1
            else:
                comp_list = arr[x+1:]
                arr[x] = max(comp_list)
        return arr
