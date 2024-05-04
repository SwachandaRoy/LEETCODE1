#removes all occurrences of a specified value val from a given array arr in-place. Here's what the code does step by step

def valpop(arr, n, val):
    i=0
    while i<n:
        if arr[i]==val:
            arr[i]=arr[n-1]
            n-=1
        else:
            i+=1
    print("New arr:", arr[:n])
    return n


arr=list(map(int, input("Enter arr:").split()))
n=len(arr)
val=int(input("Enter val:"))
print(valpop(arr, n, val))
