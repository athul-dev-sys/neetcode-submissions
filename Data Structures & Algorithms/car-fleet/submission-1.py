class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(speed)
        d={}
        for i in range(n):
            d[position[i]]=speed[i]
        st=0
        f=0
        v=sorted(d.items(),key=lambda x:x[0],reverse=True)
        for pos,sp in v:
            t=(target-pos)/sp
            if t>st:
                f+=1
                st=t
        return f