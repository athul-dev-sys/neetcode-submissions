class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=float('Inf')
        maxp=float('-Inf')
        for p in prices:
            minp=min(p,minp)
            maxp=max(maxp,p-minp)
        return maxp
        