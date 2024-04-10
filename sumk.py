#find sum of pairs that add upto k
def sumk(arr, k):
    n=len(arr)
    arr.sort()
    i=0
    j=n-1
    while i<j:
        sum1=arr[i]+arr[j]
        if sum1==k:
            return arr[i], arr[j]
        elif sum1<k:
            i+=1
        else:
            j-=1  
    return None

arr=list(map(int, input().split()))
k=int(input("Enter k:"))
print(sumk(arr, k))
