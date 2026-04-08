class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map =  defaultdict(list)

        for i in range(0,len(strs)):
            curr = ''.join(sorted(list(strs[i])))
            hash_map[curr].append(strs[i])

        print(hash_map.values())

        return list(hash_map.values())