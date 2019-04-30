def sockMerchant(n, ar):
    p = 0
    for i in range(0 , n):
        for j in range(i+1 , len(ar)):
            if ar[i] == ar[j]:
                p+=1
                ar.pop(j)
                break
    return p

print(sockMerchant(12, [2, 3, 4, 5, 4, 3, 2, 6, 2, 5, 3, 4]))
