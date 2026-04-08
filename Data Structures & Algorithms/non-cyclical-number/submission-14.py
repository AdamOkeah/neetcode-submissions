class Solution:
    def isHappy(self, n: int) -> bool:
        seen_set = set()
        while n not in seen_set and n != 1:
            seen_set.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1





        