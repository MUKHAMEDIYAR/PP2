n = input('n = ')
prod, sum = 1, 0
for i in range(len(n)):
    prod *= int(n[i])
    sum += int(n[i])
print(prod - sum)
