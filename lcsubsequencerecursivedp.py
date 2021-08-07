x = input()
y = input()

dp = [[None for i in range(len(y)+1)] for j in range(len(x)+1)]

def lcs(x, y, lx, ly):
  if(lx==0 or ly ==0):
    return 0
  
  if(dp[lx][ly]!=None):
    return dp[lx][ly]
    
    
  if(x[lx-1]==y[ly-1]):
    
    ans = 1+lcs(x, y, lx-1, ly-1)
    dp[lx][ly] = ans
    return ans
  
  
  else:
    
    ans1 = lcs(x, y, lx-1, ly) 
    ans2 = lcs(x, y, lx, ly-1)
    ans = max(ans1, ans2)
    dp[lx][ly] = ans
    return ans
     

print(lcs(x, y, len(x),len(y)))

