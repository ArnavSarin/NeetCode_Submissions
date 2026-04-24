class Solution:

    def simulate(self,piles,rate,h):
        rounds = 0
    
        for pile in piles:
            rounds += math.ceil(pile / rate)
        return rounds <= h



    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        while l<r:
            mid = l + (r-l)//2
            simulated = self.simulate(piles,mid,h)
            if simulated == True:
                r = mid
            else:
                l = mid + 1
            
        return l
        