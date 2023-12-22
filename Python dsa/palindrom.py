def pal(n):
    rev=0
    temp=n
    while temp!=0:
        lastd=temp%10
        rev=rev*10+lastd
        temp=temp//10
    return rev
n=int(input("enter number")) 
result=pal(n)
print("the palindrome is:",result)