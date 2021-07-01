nums = input().split()
txt = 0
n, k = 0, 0
while n < len(nums) - 1:
    k = n
    while k <= len(nums) - 1:
        if nums[n] == nums[k] and n < k:
            txt += 1
        k += 1
    n += 1
print(txt)
