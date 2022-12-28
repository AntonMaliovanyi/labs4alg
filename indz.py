import random
import numpy as np

n = int(input("Input N "))
t = int(input("Input T "))

def Sortlist(n, cs):
    print("\nCase", cs)
    arr = []
    arr1 = []
    med = []
    res = []

    for i in range(1, n + 1):
        arr.append(i)

    for i in range(n - 2):

        arr1.append(arr[i:i+3])
        med.append(arr1[i][random.randint(0, 2)])
        print(arr1[i])
        print("Judge responds that median is", med[i])

        temp = arr1[i][1]
        ind = arr1[i].index(med[i])
        arr1[i][1] = med[i]
        arr1[i][ind] = temp

    for i in range(n - 3):
        if arr1[i].index(arr[i+1]) < arr1[i].index(arr[i+2]) and arr1[i+1].index(arr[i+1]) > arr1[i+1].index(arr[i+2]):
            temp = arr1[i+1][0]
            arr1[i+1][0] = arr1[i+1][2]
            arr1[i+1][2] = temp
        elif arr1[i].index(arr[i+1]) > arr1[i].index(arr[i+2]) and arr1[i+1].index(arr[i+1]) < arr1[i+1].index(arr[i+2]):
            temp = arr1[i+1][0]
            arr1[i+1][0] = arr1[i+1][2]
            arr1[i+1][2] = temp

    res = res + arr1[0]

    for i in range(n - 3):
        if arr1[i+1].index(arr[i+3]) == 0:
            res.insert(0, arr1[i+1][0])
        elif arr1[i+1].index(arr[i+3]) == 2:
            res.append(arr1[i+1][2])
        else:
            res.insert(res.index(arr1[i+1][2]), arr1[i+1][1])
    return res

def Check(n, t):
    if n < 3 or t < 1:
        return -1
    else:
        return 1


if Check(n, t) == -1:
    print("Invalid N or T")
else:   
    for i in range(1, t + 1):
        print("\nResult", Sortlist(n, i))




