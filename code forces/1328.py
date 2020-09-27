def devider(a, b):    
    if a % b != 0:
        return devider(a + 1, b)
    else :
        return a 

T = int(input())

for a in range(T):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        ans = (devider(a, b) - a)
        print(ans)