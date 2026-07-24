class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        maxl=0
        seen=set()
        while right < len(s):
            while s[right] in seen:
                
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            right+=1
            maxl=max(right-left,maxl)
        return maxl