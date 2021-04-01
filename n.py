def function(n):
    arr = [ i for i in range(1,n //2 +2)]
    p1 = 0
    p2 = 1
    temp = 0
    res =[]
    while p1 < len(arr):
        temp = arr[p1]
        while p2 < len(arr) and temp <= n:
            temp += arr[p2]
            if temp == n:
                res.extend(arr[p1:p2 + 1])
                break;
            else:p2+=1
        p1+=1

    return res

print(function(15))
