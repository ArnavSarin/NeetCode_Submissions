class Solution:

    def encode(self, strs: List[str]) -> str:
        currStr = ""
        for i in strs:
            for j in range(0,len(i)):
                currStr += str(ord(i[j])) + ","
            currStr += "|"
        print(currStr)
        return currStr

    def decode(self, s: str) -> List[str]:
        arr = []
        currChar = ""
        currStr = ""
        for i in s:
            if(i != "," and i != "|"): 
                currChar += i
            elif(i == ","):
                currStr += chr(int(currChar))
                currChar = ""
            else:
                arr.append(currStr)
                currStr = ""

        return arr
                





