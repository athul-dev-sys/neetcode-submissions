class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxt=0
        while left < right:
            height=min(heights[left],heights[right])
            width=right-left
            tot=width*height
            maxt=max(maxt,tot)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxt
        