class Solution:
    def minWindow(self, s: str, t: str) -> str:
        r, l = 0,0
        ans = ''
        min_length = float('inf')

        hash_map = Counter(t)

        while r < len(s):
            if s[r] in hash_map:
                hash_map[s[r]] -= 1
            while all(v <= 0 for v in hash_map.values()):
                print("GOT HERE")
                if r-l+1 < min_length:
                    min_length = min(min_length,r-l+1)
                    ans = s[l:r+1]
                    print("GOT HERE 2")
                    print(ans)
                if s[l] in hash_map:
                    hash_map[s[l]] += 1
                l += 1
            r += 1

        return ans