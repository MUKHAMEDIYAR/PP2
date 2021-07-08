import re
inp=int(input())
for i in range(inp):
    b=input()
    x=re.findall(r"^(\+|-|\.|\d*)(\d+|\.)(\d+|\n|\.)(\d)+$",b)
    if(x):
        print("True")
    else:
        print("False")