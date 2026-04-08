class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash_map = Counter(s)
        t_hash_map = Counter(t)

        return s_hash_map == t_hash_map 
            

        