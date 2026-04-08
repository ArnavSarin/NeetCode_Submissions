class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        
        for i in range (0,len(nums)):
            if(i==0):
                res[1:]= [j * nums[i] for j in res[1:len(nums)]]
                print("GOT HERE 1:")
                print(res)
            elif(i==len(nums)-1):
                res[:-1]= [j * nums[i] for j in res[0:-1]]
                print("GOT HERE 2:")
                print(res)
            else:
                res[:i+1]= [j * nums[i] for j in res[:i]]
                res[i+1:]= [j * nums[i] for j in res[i:]]
                print("GOT HERE 3:")
                print(res)
        return res

            

            

