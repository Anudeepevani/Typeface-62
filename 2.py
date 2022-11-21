def solve(a,b):
    count,length=0,0
    for i in b:
        length+=1
    last_character=b[length-1]
    for i in a:
        if i==last_character:
            count+=1
    return count
a=input()
b=input()
print(solve(a,b))
