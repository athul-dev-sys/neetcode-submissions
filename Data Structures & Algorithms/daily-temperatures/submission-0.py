class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        ans=[0]*n
        for t in range(len(temperatures)):
            while stack and temperatures[t]>temperatures[stack[-1]]:
                a=stack.pop()
                ans[a]=t-a
            stack.append(t)
        return ans

        