class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        bestLength = 0
        curr = ""

        for idx, i in enumerate(s):
            if(i not in curr):
                curr += i
            else:
                # curr = i

                # ptr+=1
                # curr = curr[ptr:idx]
                #Should be last index where i was seen -> i
                # lastIdx = curr.rfind(i)+1
                print("currBefore: " + curr)
                lastIdx = curr.rfind(i)+1
                if(lastIdx == idx):
                    curr = i
                else: 
                    curr = curr[lastIdx:idx]+i
                print("lastIdx: " + str(lastIdx) + " idx: " + str(idx))
                print(curr)

            bestLength = max(bestLength,len(curr))
        return bestLength

        