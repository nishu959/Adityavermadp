n = int(input()) 

val = list(map(int, input().split()))

wt = list(map(int, input().split())) 

W= int(input())

dp = [[None for i in range(W+1)] for j in range(n+1)]

def unboundedknapsack(val,wt,n,W,dp):
  if(n==0 or W==0):
    return 0
  
  if(dp[n][W]!=None):
    return dp[n][W]
    
  
  if(W >=wt[n-1]):
    ans1 =val[n-1] + unboundedknapsack(val,wt,n,W-wt[n-1],dp)
    ans2 = unboundedknapsack(val,wt,n-1,W,dp)
    ans = max(ans1, ans2) 
    dp[n][W]=ans
    return ans
    
  else:
    ans = unboundedknapsack(val,wt,n-1,W,dp)
    dp[n][W]=ans
    return ans
    
    
print(unboundedknapsack(val,wt,n,W,dp))

