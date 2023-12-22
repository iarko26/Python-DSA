#input is 3 and output is 6
"""
def sum(n):
    total_sum=0
    for i in range(1,n+1):
        total_sum=total_sum+i
    return total_sum
n=int(input("enter the number of n:"))
result=sum(n)
print("The output:",result)
"""

# sum of natural numbers for  10 days
def sum_of_days(n):
    
    total_sum=n*(n+1)//2
    return total_sum
n=int(input("number of days:"))
result=sum_of_days(n)
print("the number of n days:",result)