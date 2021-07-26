"""
X = "abcdgh"
Y = "abedfggr"

Longest common substring = ab

Longest common Subsequence = abdh

here in question we have to return length of
Longest common Subsequence

#continuous same
"""
m = int(input())
x = input()
n= int(input())
y = input() 
past=[[None for i in range(n+1)] for j in range(m+1)]



def lcs(x, y, m, n, past):
  if(m==0 or n==0):
    past[m][n]= 0
    return 0
  
  if(past[m][n]!=None):
    return past[m][n]
    
  
  if(x[m-1]==y[n-1]):
    ans = lcs(x, y, m-1,n-1, past) + 1
    past[m][n]= ans
    
    return ans
  else:
    ans1 = lcs(x, y, m-1,n, past)
    ans2 = lcs(x, y, m,n-1, past)
    ans = max(ans1, ans2)
    past[m][n]= ans
    return ans
   
  
print(lcs(x, y, m, n, past))