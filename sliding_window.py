import sys
k = int(input("Enter Window Size: "))

lst= [2,14,1,34,22,12,5,3]

wSum = 0
mxSum = -sys.maxsize - 1 # MinNegativeInteger
if(k>len(lst)):
    print()

for i in range(k):
    wSum += lst[i]
mxSum = max(wSum,mxSum)

#Static Window

for j in range(k,len(lst)-1,1):
    wSum = wSum - lst[j-k] + lst[j]
    mxSum = max(wSum,mxSum)

#Window End

print("Max Sum of a Subarray of the size {} is : {} ".format(k,mx))
