#Question3
list_input=input("Enter elements of list eg(1 2 3):\n").split()
l=[int(i) for i in list_input]
l.sort()
ele=int(input("Enter element to be searched:\n"))
first=0
last=len(l)
pos=-1
for i in range(first,last):
    mid=int(first+last/2)
    if(ele==l[mid]):
        pos=mid
        break
    if ele>l[mid]:
        first=mid+1
    if ele<l[mid]:
        last=mid-1
if pos==-1:
    print("\nElement not found.")
else:
    print("\nElement found at ",pos)
