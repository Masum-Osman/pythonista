# n = int(input())
# k = 0
k = int(input())

# for i in range(1, n+1):
#     if i%2 != 0:
#         k = k - i
#     else:
#         k = k + i

if k%2 == 0:
    k = k / 2
else:
    k = (k - 1)/ 2 - k

print(int(k))