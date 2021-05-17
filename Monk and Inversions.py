#code monk problem on hackerearth


t=int(input())
while t:
    n=int(input())
    cnt=0
    # for i in range(n):
    #         mat[i]=[int(j) for j in input().split()]
    # one-liner logic to take input for rows and columns
    mat = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        mat[i]=[int(j) for j in input().split()]
    m,l=[],[]
    for i in range(n):
        for j in range(n):
            m.append((i, j))
            l.append((i, j))

    for i, j in m:
        for p, q in l:
            if i <= p and j <= q and mat[i][j] > mat[p][q]:
                    cnt += 1

    print(cnt,end='\n')
    t=t-1
