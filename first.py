n=int(input("Enter number of elements in main array: "))
print("Enter elements :")
arr1=[]
for i in range(0,n):
        z=int(input())
        arr1.append(z)

m=int(input("Enter number of elements in subarray: "))
print("Enter elements :")
arr2=[]
for i in range(0,m):
        z=int(input())
        arr2.append(z)


hash={}
for i in range(0,n):
        if arr1[i] not in hash:
                hash[arr1[i]]=True
        
count=0
for i in range(0,m):
        if arr2[i] in hash:
           count =1
        else:   
                count=0
                print("Array 2 is not a subset of array1 ")
                break

if(count==1):
        print("Array 2 is a subset of array1 ")
