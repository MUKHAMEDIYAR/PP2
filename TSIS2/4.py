gain = input().split()
for i in range(len(gain)):
    gain[i] = int(gain[i])
sum = 0
att = [0]
for i in range(len(gain)):
    sum += gain[i]
    att.append(sum)
if max(att) < 0:
    print(0)
else:
    print(max(att))