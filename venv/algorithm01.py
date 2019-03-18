def def1(arr):
    result = []

    be = True
    for a in arr:
        if be:
            result.append(a)
            be = False
            continue

        if result[-1] != a:
            result.append(a)

    print(result)


arr1 = [1, 1, 3, 3, 0, 1, 1]
def1(arr1)

arr2=[4, 4, 4, 3, 3]
def1(arr2)