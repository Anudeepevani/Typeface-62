def check(n):
    while(n>0):
        c=n%10
        if(c==3 or c==4 or c==7):
            return False
        n//=10
    return True
    
def number(n):
    c,count=1,1
    while(count<n):
        c+=1
        if(check(c)):
            count+=1
    return c
    
n=int(input())
print(number(n))
