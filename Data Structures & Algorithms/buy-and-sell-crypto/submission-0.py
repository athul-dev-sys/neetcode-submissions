class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        pr=float('-Inf')
        for p in prices:
            minp=min(minp,p)
            pr=max(pr,p-minp)
        return pr
        