class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = {}
        def solve(a,b):
            if a==b:
                return True
            if len(a)<=1 or len(b)<=1:
                return False
            
            key = a + " " + b
            if key in dp:
                return dp[key]
            n = len(a)
            flag = False
            for i in range(1, n):
                cond1 = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
                cond2 = solve(a[:i], b[:i]) and solve(a[i:], b[i:])
                if cond1 or cond2:
                    flag = True
                    break
            dp[key]=flag
            return flag
            






        if (len(s1)!=len(s2)):
            return False;
        if len(s1)==0:
            return True
        ans = solve(s1,s2)
        return ans

        
