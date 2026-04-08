class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        checklist = list(range(0, n+1))
        correct_sum = sum(checklist)
        actual_sum = sum(nums)

        return correct_sum - actual_sum
