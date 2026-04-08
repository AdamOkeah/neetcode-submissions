class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = Counter(s)
        t_freq = Counter(t)

        if len(s_freq) != len(t_freq):
            return False
        anagram = True
        for key, value in s_freq.items():
            if s_freq[key] != t_freq[key]:
                anagram = False
        return anagram
                
                

            


        
        