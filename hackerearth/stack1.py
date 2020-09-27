T = int(input())

s = []

while T > 0:
    val = input()
    splited = list(val)
    for i in splited:
        s.append(i)
    print(s)
    T = T -1