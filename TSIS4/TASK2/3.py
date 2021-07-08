import re
#x = re.findall(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]",s)
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
if a:
    for sub in a:
        print(sub)
else: print(-1)