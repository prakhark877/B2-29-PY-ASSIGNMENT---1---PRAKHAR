def reverse(arr, k):

    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    arr[:] = arr[::-1]

listx = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 4
print("Original list:",listx)
reverse(listx,value)
print("Reversed list:",listx)