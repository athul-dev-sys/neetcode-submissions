class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key={}
        for i in s1:
            key[i]=key.get(i,0)+1
        left=0
        co={}
        for right in range(len(s2)):
            co[s2[right]]=co.get(s2[right],0)+1
            if right-left+1>len(s1):
                co[s2[left]]-=1
                if co[s2[left]]==0:
                    del co[s2[left]]
                left+=1
            if co==key:
                return True
        return False
            
            

        