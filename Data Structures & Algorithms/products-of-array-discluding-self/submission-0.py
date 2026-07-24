class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        s=1
        n=len(nums)
        ans=[1]*n
        for i in range(n):
            ans[i]=p
            p*=nums[i]
        for i in range(n-1,-1,-1):
            ans[i]*=s
            s*=nums[i]

        return ans
        