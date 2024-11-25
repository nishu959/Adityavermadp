class Solution:
    
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[None for i in range(n+1)] for j in range(k+1)]
        import sys
        def fun(e, f):
            if f==0 or f==1:
                return f
            if e ==1 :
                return f

            if dp[e][f]!=None:
                return dp[e][f]
            
            mn = sys.maxsize
            low = 1
            high = f
            while (low <= high):
                mid = (low + high)//2
                left =0
                right =0
                tempans = 0
                if dp[e-1][mid-1]!=None:
                    left = dp[e-1][mid-1]
                else:
                    left = fun(e-1,mid-1)
                    dp[e-1][mid-1] = left

                if dp[e][f-mid]!=None:
                    right = dp[e][f-mid]
                else:
                    right = fun(e,f-mid)
                    dp[e][f-mid] = right
                
                if(right > left):
                    low = mid +1
                    tempans = 1 + right
                else:
                    high = mid -1
                    tempans = 1 + left

                mn = min(mn , tempans)
            
            dp[e][f] = mn
            return mn


        ans  =fun(k,n)
        return ans
            

        
