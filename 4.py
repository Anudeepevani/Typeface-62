def solve(matrix):
    g = len(matrix)
    left,top,right,bottom = g-1,g-1,0,0
    for a in range(g):
        for b in range(g):
            if matrix[a][b]==0:
                left = min(left,b)
                top = min(top,a)
                right = max(right,b)
                bottom = max(bottom,a)
    return [(top,left),(top,right),(bottom,left),(bottom,right)]
    
lt = []
n1 = 256
for i in range(n1):
    lt.append(list(map(int,input().split())))
print(solve(lt))
