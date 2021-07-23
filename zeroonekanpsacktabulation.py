n = int(input())

val = list(map(int, input().split()))

wt = list(map(int, input().split()))

W = int(input())
past = [[None for i in range(W+1)] for j in range(n+1)]

for i in range(n+1):
  for j in range(W+1):
    
    if(i==0 or j==0): 
      past[i][j] = 0
      
    elif(j>=wt[i-1]):
      
      past[i][j]=max(val[i-1]+past[i-1][j-wt[i-1]],past[i-1][j])
     
    else:
      
      past[i][j] = past[i-1][j]
     
    
print(past[n][W])