#remove duplicates from array
'''consider array as linked list, use floyd's cycle tortoise hare algorithm
each node points to node having its own value as index.
1st cycle until they meet: tortoise+=1, hare+=2
reset index of tortoise to 0
2nd cycle until they meet: tortoise+=1, hare+=1.
This returns first duplicate node (first node of cycle)'''

def nodup(arr):
    tortoise=arr[0]
    hare=arr[arr[0]]
    while tortoise!=hare:
        tortoise=arr[tortoise]
        hare=arr[arr[hare]]
    tortoise=0
    while tortoise!=hare:
        tortoise=arr[tortoise]
        hare=arr[hare]
    return tortoise

arr=list(map(int, input().split()))
print(nodup(arr))
