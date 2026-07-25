class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        curr={}
        maxl=0
        maxf=0
        for right in range(len(s)):
            curr[s[right]]=curr.get(s[right],0)+1
            maxf=max(maxf,curr[s[right]])
            while (right-left+1)-maxf >k:
                curr[s[left]]-=1
                left+=1
            maxl=max(maxl,right-left+1)
        return maxl
                