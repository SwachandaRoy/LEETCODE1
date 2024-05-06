def buyandsell(prices):
    left=0
    right=1
    maxprofit=0
    while right<len(prices):
        if prices[left]>prices[right]:
            left+=1
            right+=1
        else:
            curprofit=prices[right]-prices[left]
            maxprofit=max(curprofit, maxprofit)

    return maxprofit

prices= [7,3,5,1,6,4]
print(buyandsell(prices))

