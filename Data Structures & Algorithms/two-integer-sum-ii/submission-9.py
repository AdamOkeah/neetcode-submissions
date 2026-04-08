class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = set()
        l = 0
        r = len(numbers) - 1
        current_value = 0
        while l < r:
            current_value = numbers[l] + numbers[r]

            if  current_value < target:
                l += 1

            if current_value > target:
                r -= 1

            if current_value == target:
                return [l+1, r+1]

        
            

                
            

                
        