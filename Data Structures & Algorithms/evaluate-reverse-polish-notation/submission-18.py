class Solution:
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        arr = []

        if(len(tokens) == 0):
            return 0

        if(len(tokens) == 1):
            return int(tokens[0])

        for i in range(0,len(tokens)):
            arr.append(tokens[i])
            print(arr)

            if(not self.is_number(arr[-1])):
                sign = arr.pop()
                firstVal = int(arr.pop())
                secondVal = int(arr.pop())

                if(sign == '+'):
                    secondVal += firstVal
                elif(sign == '-'):
                    secondVal -= firstVal
                elif(sign == '*'):
                    secondVal *= firstVal
                elif(sign == '/'):
                    secondVal /= firstVal
                arr.append(int(secondVal))

        return arr.pop()
                
              


            
        
        