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
                print("first case: " + i)
                currChar += i
            elif(i == ","):
                print("second case: " + currChar)
                currStr += chr(int(currChar))
                print("second case: " + currStr)
                currChar = ""
            else:
                print("third case: " + currStr)
                arr.append(currStr)
                currStr = ""

        return arr
                





