n = int(input())

coin = list(map(int, input().split()))

target = int(input())

dp = [[None for i in range(target+1)] for j in range(n+1)]

def coinchange(coin, n, W):
  
  if(W==0 ):
    return 1
    
  if(n==0):
    return 0
  
  if(dp[n][W]!=None):
    return dp[n][W]
    
  
  if(W >= coin[n-1]):
    ans1 = coinchange(coin, n, W-coin[n-1])
    ans2 = coinchange(coin, n-1, W)
    ans = ans1 + ans2
    dp[n][W] = ans
    return ans
   
  
  else:
    ans = coinchange(coin, n-1, W)
    dp[n][W] = ans
    return ans
   
 
print(coinchange(coin, n, target))

