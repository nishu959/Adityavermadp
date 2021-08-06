n = int(input())

length = list(map(int, input().split()))


price = list(map(int, input().split()))

dp = [[None for i in range(n+1)] for j in range(n+1)]

def rcp(length, price, p, q):
  
  if(p==0 or q==0):
    return 0
  
  if(dp[p][q]!=None):
    return dp[p][q]
   
  
  if(q>=length[p-1]):
    
    ans = max(price[p-1] + rcp(length, price, p, q-length[p-1]) , rcp(length, price, p-1, q))
   
    dp[p][q] = ans
    return ans
   
 
  else:
    
    ans = rcp(length, price, p-1, q)
   
    dp[p][q] = ans
    return ans
   
 
print(rcp(length, price, n, n))


