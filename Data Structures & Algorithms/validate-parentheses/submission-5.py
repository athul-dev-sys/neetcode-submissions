class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        d={')':'(',']':'[','}':'{'}
        st=[]
        for c in s:
            if c in d:
                if not st or st.pop()!=d[c]:
                    return False
            else:
                st.append(c)
        if st:
            return False
        return True
        