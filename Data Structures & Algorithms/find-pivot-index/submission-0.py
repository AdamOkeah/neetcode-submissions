class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        for x in range(len(nums)):
            if sum(nums[:x]) == sum(nums[x+1:]):
                return x
                
        return -1
            
                
                

        