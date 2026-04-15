class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0

        if len(tokens)==1 and tokens[0].isdigit():
            return int(tokens[0])

        for i in range (0,len(tokens)):
            if len(tokens[i]) > 1 and tokens[i][0] == '-' or tokens[i].isdigit():
                stack.append(int(tokens[i]))         
            else:
                if len(stack)>=2:
                    value_2 = int(stack.pop())
                    value_1 = int(stack.pop())
                    if tokens[i] == '+':
                        value = value_1 + value_2
                    elif tokens[i] == '-':
                        value = value_1 - value_2 
                    elif tokens[i] == '*':
                        value = value_1 * value_2
                    else:
                        value = value_1 / value_2
                    stack.append(int(value))

        return stack[0]


