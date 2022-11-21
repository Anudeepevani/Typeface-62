def trinary(n):
    ans,k='',''
    while(n>0):
        c=n%3
        ans=str(c)+ans
        n//=3
    return ans
    
n=int(input())
print(trinary(n))
