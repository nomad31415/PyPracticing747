def maxProfitWithKTransactions(prices, k):
    # Write your code here.

    cnt = 0
    tmp = prices[:(2*k - 1)]
    zz = sum([x for i,x in  enumerate(tmp) if i % 2 == 0 ])



    if len(prices) > k * 2:
        cnt = sum(tmp) - 2*zz + max(prices)
    else:
        cnt = sum(prices[:k*2]) - 2*zz


    return cnt



if  __name__ == '__main__':
    k = 2

    #prices = [5,11,3,50,60,90]
    prices = [5,11,3,50]


    maxProfitWithKTransactions(prices, k)    
