class Solution:
    def isValid(self, s: str) -> bool:
        data = []
        for i in s:
            print(data)
            if(len(data)!=0):
                if(data[len(data)-1] == '(' and i == ')'):
                    data.pop()
                elif(data[len(data)-1] == '{' and i == '}'):
                    data.pop()
                elif(data[len(data)-1] == '[' and i == ']'):
                    data.pop()
                else:
                    data.append(i)
            else:
                data.append(i)
        return len(data) == 0
            
        