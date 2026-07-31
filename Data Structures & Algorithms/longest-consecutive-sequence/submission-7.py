class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxc=0
        s=set(nums)
        if not nums:
            return 0
        for n in s:
            if n-1 not in s:
                c=1
                curr=n+1
                while curr in s:
                    c+=1
                    curr+=1
                maxc=max(c,maxc)

        return maxc
        