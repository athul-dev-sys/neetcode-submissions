class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(k):
            ho=0
            for p in piles:
                ho+=p//k
                if p%k>0:
                    ho+=1
            if ho<=h:
                return True
        left,right=1,max(piles)
        while left<=right:
            mid=(left+right)//2
            if valid(mid):
                right=mid-1
            else:
                left=mid+1
        return left
              
        