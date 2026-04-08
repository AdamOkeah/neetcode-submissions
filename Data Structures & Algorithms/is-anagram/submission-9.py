class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = Counter(s)
        t_freq = Counter(t)

        if len(s_freq) != len(t_freq):
            return False

        return s_freq == t_freq
                
                

            


        
        