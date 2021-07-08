import re
k = int(input())
d = []
for i in range(k):
    s = input().split()
    x = re.search(r"^\<([a-zA-Z][a-zA-Z0-9-_.]*[a-zA-Z0-9]\@[a-zA-Z]+\.[a-z]{1,3})\>$",s[1])
    if x:
        d.append(s[0]+" "+s[1])
for i in d:
    print(i)