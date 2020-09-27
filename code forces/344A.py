T = int(input())

count = 0

for a in range(T):
    m = input()
    if m == "01":
        count += 1
    elif m == "10":
        count += 1

print(count)  