n = int(input())

val = list(map(int, input().split()))

wt = list(map(int, input().split()))

W = int(input())
past = [[None for i in range(W+1)] for j in range(n+1)]


def kanpsack(val, wt, n, W, past):
  if(n==0 or W==0):
    past[n][W] = 0
    return 0
  
  if(past[n][W]!=None):
    return past[n][W]
  
  
  if(wt[n-1]<=W):
    ans = max( val[n-1] +kanpsack(val, wt, n-1, W-wt[n-1], past), kanpsack(val, wt, n-1, W, past))
    past[n][W] = ans
    return ans
  else:
    ans = kanpsack(val, wt, n-1, W, past)
    past[n][W] = ans
    return ans
   
   


print(kanpsack(val, wt, n, W, past))


