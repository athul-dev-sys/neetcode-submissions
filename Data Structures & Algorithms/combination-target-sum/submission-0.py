class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def back(ind,path,tar):
            if tar==0:
                res.append(path[:])
                return
            if ind==len(nums) or tar<0:
                return
            path.append(nums[ind])
            back(ind,path[:],tar-nums[ind])
            path.pop()
            back(ind+1,path,tar)
        back(0,[],target)
        return res
        