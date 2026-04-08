class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str_pt_uno = ''
        encoded_str_pt_dos = '' 
        for i in range(0,len(strs)):
            encoded_str_pt_uno += str(len(strs[i])) + ','
            encoded_str_pt_dos += strs[i]
        return encoded_str_pt_uno + '#' + encoded_str_pt_dos



    def decode(self, s: str) -> List[str]:
        ans = []
        lengths = []
        current_num = 0
        starting_idx = 0
        for i in range(0,len(s)):
            if s[i] == '#':
                starting_idx = i+1
                break
            elif s[i] == ',':
                lengths.append(current_num)
                current_num = 0
            else:
                current_num = ((current_num*10) + int(s[i]))

        for i in range(0,len(lengths)):
            if(lengths[i]==0):
                ans.append('')
            else:
                ans.append(s[starting_idx:starting_idx+lengths[i]])
                starting_idx = starting_idx + lengths[i]
    
        return ans

                






