import sys
n = int(input())
coin = list(map(int, input().split()))
target = int(input())


past = [[None for i in range(target+1)] for j in range(n+1)] 

def coinch2(coin, n, target, past):
  if(target ==0 and n!=0):
    past[n][target] = 0
    return 0
    
  if(n==1):
    if(target%coin[0]==0):
      past[n][target] = target//coin[0]
      return target//coin[0]
     
    else:
      past[n][target] = sys.maxsize - 1
      return sys.maxsize - 1
  
  if(past[n][target]!=None):
    return past[n][target]
  
    
  
  if(target >=coin[n-1]):
    ans1 = coinch2(coin, n, target-coin[n-1], past)+1
    ans2 = coinch2(coin, n-1, target, past)
    ans = min(ans1, ans2)
    past[n][target] = ans
    return ans
    
  else:
    ans= coinch2(coin, n-1, target, past)
    past[n][target] = ans
    return ans
   
  
 
print(coinch2(coin, n, target, past)) 
  