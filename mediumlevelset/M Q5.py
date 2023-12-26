def getMin(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = min(res, arr[i])
    return res
def getMax(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = max(res, arr[i])
    return res

arr = [25, 28, 21, 24, 27]
n = len(arr)
print("Average Tempertaure : ",sum(arr)/n)
print ("Lowest Temperature : ", getMin(arr, n))
print ("Highest Temperature : ", getMax(arr, n))