class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []
    
        
    def push(self, val: int) -> None:
        if(len(self.arr) == 0 or val <= self.getMin()):
            self.minArr.append(val)
        self.arr.append(val)
        print("push" + str(self.arr))
        print("push getMin" + str(self.minArr))
        

    def pop(self) -> None:
        if(len(self.arr) != 0):
            if(self.arr[len(self.arr)-1] == self.getMin()):
                self.minArr.pop()
            self.arr.pop() 
        print("pop" + str(self.arr))
        print("pop getMin" + str(self.minArr))


    def top(self) -> int:
        if(len(self.arr) != 0):
            return self.arr[len(self.arr)-1]
        

    def getMin(self) -> int:
        if(len(self.minArr)!= 0):
            return self.minArr[len(self.minArr)-1] 
        return



        
