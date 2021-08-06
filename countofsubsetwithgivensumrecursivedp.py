n =int(input())

l = list(map(int, input().split()))
  

target = int(input())


past = [[None for i in range(target+1)] for j in range(n+1)]

def subsetsum(n, target, past):
  if(target ==0):
    past[n][target] = 1
    
    return 1
  
  if(n==0):
    past[n][target] = 0
    return 0
 
  
  
  if(past[n][target]!=None):
    return past[n][target]
    
  if(l[n-1]<=target):
    ans= subsetsum(n-1, target-l[n-1], past)  + subsetsum(n-1, target, past)  
    past[n][target] = ans
    return ans
  else:
    
    ans = subsetsum(n-1, target, past)
    past[n][target] = ans
    return ans
 
 
print(subsetsum(n, target, past))