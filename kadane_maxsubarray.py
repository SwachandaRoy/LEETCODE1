def kadane(arr1):
    max_curr=max_global=arr[0]
    for ele in arr[1::]:
        max_curr=max(ele, max_curr+ele)
        max_global=max(max_curr, max_global)
    return max_global

arr=list(map(int, input("Enter array:").split()))
print("SOL: ",kadane(arr))


