#eg: [-2, 1, -3]

def kadane(arr1):
    curr_sum=0
    max_sum=arr[0]
    for ele in arr1:
        curr_sum=max(ele, max_curr+ele)
        max_sum=max(max_sum, curr_sum)
    return max_sum

arr=list(map(int, input("Enter array:").split()))
print("SOL: ",kadane(arr))


