import sys
n = int(input())
coin = list(map(int, input().split()))
target = int(input())


past = [[None for i in range(target+1)] for j in range(n+1)] 


for i in range(n+1):
  for j in range(target+1):
    
    if(i==0):
      past[i][j] = sys.maxsize - 1
      
    elif(j==0):
      past[i][j] = 0
     
    elif(i==1):
      if(j%coin[0]==0):
        past[i][j]= j//coin[0]
        
    else:
      if(j >= coin[i-1]):
        ans1 =past[i][j-coin[i-1]]+1
        ans2 =  past[i-1][j]
        ans = min(ans1, ans2)
        past[i][j]= ans
        
      else:
        ans =  past[i-1][j]
        past[i][j]= ans
     
    
   
print(past[n][target])