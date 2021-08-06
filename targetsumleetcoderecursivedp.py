#code is same as count of subsets with given difference 
# where given diff = sum
#[1,1,2,3]
#for sum = 1
#+1-1-2+3-> +ve 3,1 -ve 1,2
#difference of subsets of 3,1 and 1,2


n = int(input())
l = list(map(int, input().split()))
diff = int(input())

s = sum(l) + diff

W= s//2

dp = [[None for i in range(W+1)] for j in range(n+1)]

def subsetsum(l, n, W):
  
  if(W==0):
    return 1
   
  if(n==0):
    return 0
   
  
  if(dp[n][W]!=None):
    return dp[n][W]
  
  
    
  if(W >= l[n-1]):
    ans = subsetsum(l, n-1, W-l[n-1]) + subsetsum(l, n-1, W)
    dp[n][W] = ans
    return ans
    
  else:
    ans = subsetsum(l, n-1, W)
    dp[n][W] = ans
    return ans
    
 
print(subsetsum(l, n, W))
 