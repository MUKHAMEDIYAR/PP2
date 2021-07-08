import re
s = input()
x = re.split(r"[\.|\,]",s)
for i in x:
    print(i)