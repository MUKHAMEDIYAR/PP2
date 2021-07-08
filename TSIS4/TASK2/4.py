import re
k = int(input())
for i in range(k):
    s = input()
    x = re.search(r"^[789]\d{9}$",s)
    if x:
        print("YES")
    else:
        print("NO")
