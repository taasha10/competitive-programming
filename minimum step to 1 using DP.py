# using memoization

n = 9
dp = [-1]*(n+1)
def getMinSteps(n):
    if n==1: 
        print("res:",0,"for n=",n)
        return 0
    if dp[n]!= -1 : 
        print("dp[n]",dp[n],"for n=",n)
        return dp[n] # we will already have the data in memoization like for dp[4] it will look for dp[2]
    
    res = 1 +getMinSteps(n-1) #generic step if it's neither divisible by 2 nor with 3 ; max value = n
    
    print('res:',res, "for n=",n)
    
    if n%2 == 0:
        res = min(res, 1+getMinSteps(n//2)) # if it's divisible by 2 then find min between the generic and /2 value
        print('res 2:',res, "for n=",n)
    if n%3 == 0:
        res = min(res, 1+getMinSteps(n//3)) #same as above for /3
        print('res 3:',res,"for n=",n)
        
    dp[n]=res # this step will keep updating the result until we reach our final value
    print("dp:",dp)  
    return res   # final result

print(getMinSteps(n))


#using Table 

n=9
dp = [-1]*(n+1)   #-1 default value if the table value is not updated yet

dp[1]=0  #base case

# self-explanatory loop from 2 to n ; refer memoization for detailed comments 
#added print statements are there to understand the code flow

for i in range(2,n+1):
    dp[i] = 1+ dp[i-1]
    print("og dp:",dp[i])  
    if i%2 == 0:
        dp[i] = min(dp[i],1+dp[i//2])
        print("/2:",dp[i])
    if i%3 == 0:
        dp[i] = min(dp[i],1+dp[i//3])
        print("/3:",dp[i])

print(dp[n])
