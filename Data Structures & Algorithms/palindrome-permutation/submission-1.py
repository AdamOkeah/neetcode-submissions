class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
      freq_map = Counter(s)

      odds = sum(x % 2 for x in freq_map.values())

      return odds <= 1