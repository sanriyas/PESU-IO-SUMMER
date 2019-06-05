#Question4
n=int(input("Enter number: "))
s=0
while(n>0):
    r=int(n%10)
    s=s+r
    n=n/10
print("Sum: ",s)
