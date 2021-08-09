import sys

n =int(input())

l = list(map(int, input().split()))

def solve(l, i, j):
  mn =  sys.maxsize 
  
  if(i >=j):
    return 0
  
  
  
  for k in range(i, j):
    
    temp = solve(l, i, k) + solve(l, k+1, j) + l[i-1] * l[k] * l[j]      
    
    mn = min(mn, temp)
   
 
  return mn
 

print(solve(l, 1, n-1))


