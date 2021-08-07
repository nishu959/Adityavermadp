import sys

n = int(input())

coin = list(map(int, input().split()))

target = int(input())

dp = [[None for i in range(target+1)] for j in range(n+1)]


def coinchange2(coin, n, W):
  
  #n==0 optional
  if(n==0):
    return sys.maxsize-1
  
  if(W==0):
    return 0
    
  if(n==1):
    if(W % coin[0]==0):
      return W//coin[0]
      
    else:
      return sys.maxsize - 1
      
  if(dp[n][W]!=None):
    return dp[n][W]
  
  
 
  if(W>= coin[n-1]):
    ans1 = coinchange2(coin, n, W-coin[n-1]) + 1
    ans2 = coinchange2(coin, n-1, W) + 0
    ans = min(ans1, ans2)
    dp[n][W] = ans
    return ans
 
  else:
    ans = coinchange2(coin, n-1, W)
    dp[n][W] = ans
    return ans
   
  
print(coinchange2(coin, n, target))


