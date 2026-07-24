class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxl=0
        for num in nums:
            if num-1 not in nums:
                curr=num
                i=1
                while curr+1 in nums:
                    i+=1
                    curr+=1
                maxl=max(maxl,i)
        return maxl
        