n = input('command = ')
k = ""
an = ""
h = {"G" : "G", "()" : "o", "(al)" : "al"}
for i in range(len(n)):
    k += n[i]
    if k in h:
        an += h[k]
        k = ""
print(an)
