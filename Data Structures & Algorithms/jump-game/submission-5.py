class Solution:

    def canJumpHelper(self,idx,nums:List[int]):
        check = False
        if(idx>=len(nums)-1):
            print("GOT HERE 1")
            return True
        elif(idx+nums[idx]==idx):
            print("GOT HERE 2")
            return False

        print("idx: " + str(idx))
        print("NUMS[idx]: " + str(nums[idx]))
        for i in range(1,nums[idx]+1):
            print("I:" + str(i))
            if(self.canJumpHelper(idx+i,nums)):
                check=True
        return check


    def canJump(self, nums: List[int]) -> bool:

        return self.canJumpHelper(0,nums)
    
        # idx = 0
        # if(len(nums)<=1):
        #     return True
        # while(idx<=len(nums)-1):
        #     print(idx)
        #     jump = nums[idx]
        #     if(idx+jump==(len(nums)-1)):
        #         print("GOT HERE")
        #         return True
        #     if(idx+jump==idx):
        #         print("GOT HERE 2")
        #         return False
        #     idx+=jump
        # return True
        




        