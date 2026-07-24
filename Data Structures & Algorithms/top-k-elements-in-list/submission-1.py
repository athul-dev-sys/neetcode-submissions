class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i,num in enumerate(nums):
            d[num]=d.get(num,0) +1
        s=sorted(d.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for j in range(k):
            ans.append(s[j][0])
        return ans