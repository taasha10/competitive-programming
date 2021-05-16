t=int(input())
while t:
    n,k=input().split()
    n,k=int(n),int(k)
    arr1,arr2 = []*n,[0]*n
    arr1 = [int(item) for item in input().split()]
    for i in range(len(arr1)):
        arr2[(i+k)%n]=arr1[i]

    for num in arr2:
        print(num,end=' ')
    t=t-1
    print(end='\n')
