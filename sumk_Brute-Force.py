#find sum of pairs that add upto k
def sumk(arr, k):
    n=len(arr)
    flag=False
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j]==k:
                print("Pairs:", arr[i], "&", arr[j])
                flag=True
    if flag==False:
        print("No pair")
        return
    
arr=list(map(int, input().split()))
k=int(input("Enter k:"))
sumk(arr, k)