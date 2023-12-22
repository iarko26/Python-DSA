"""
def factorial(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res
n=int(input("enter the number"))
result=factorial(n)
print("factorial of n is:",result)

"""
#recursive with digit count
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
        
    
   
        
    
n=int(input("enter the Number:"))
result=factorial(n)
print("factorial:",result)
count=0
temp=result
while temp>0:
    count+=1
    temp=temp//10
print(count)


    








    
    