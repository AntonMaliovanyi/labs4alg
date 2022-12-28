from re import findall

def splitlist(lst):

    if len(lst)<=2:
        lst1 = lst[0]
        lst[0] = lst[-1]
        lst[-1] = lst1
        return lst

    else:
        midpoint = len(lst) // 2
        lst = [lst[:midpoint], lst[midpoint:]]
        lst[0] = splitlist(lst[0])
        lst[1] = splitlist(lst[1])
        print(lst)
        lst1 = lst[0]
        lst[0] = lst[-1]
        lst[-1] = lst1
        lst = lst[0] + lst[1]
    return lst


def msort(lst, left, right):
    if len(lst == 1):
        return lst

        



a = str(input())

a = splitlist(findall(r'\d', a))

for i in range(len(a)):
    print(int(a[i]), end = "")


