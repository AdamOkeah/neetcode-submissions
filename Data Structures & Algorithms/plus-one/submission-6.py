class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = list(map(lambda x: str(x), digits))
 

        num = ''.join(strings)
        num = int(num) + 1

        digits =  list(int(digit) for digit in str(num))
        return digits
       
        