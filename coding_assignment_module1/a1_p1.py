#Question 1
s=input("Enter sequence of comma separated values:\n")
l=[int(x) for x in s.split(",")]
t=tuple(l)
print("List: ",l,"\nTuple: ",t)
