class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        checklist = set(range(0,n+1))
        num = [int(x) for x in checklist if x not in nums]
        return num[0]