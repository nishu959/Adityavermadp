m = int(input())
x = input()
n= int(input())
y = input() 
past=[[None for i in range(n+1)] for j in range(m+1)]


for i in range(m+1):
  for j in range(n+1):
    if(i==0 or j==0):
      past[i][j] = 0
      
    elif(x[i-1]==y[j-1]):
      past[i][j] = 1 + past[i-1][j-1] 
      
    else:
      past[i][j] = max(past[i-1][j],past[i][j-1])
      
      
      
print(past[m][n])
      
  