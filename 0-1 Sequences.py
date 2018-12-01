s = input()
mod = 1000000007
seenq = seen1 = total = 0
prev = pow2 = 1

for i in s:
    if i == '?':
        total = (total * 2 % mod) + (seen1 * pow2 % mod)
        total %= mod
        total += (seenq * (prev)) % mod
        total %= mod
        seenq += 1
        prev = pow2
        pow2 *= 2
        pow2 %= mod
    if i == '1':
        seen1 += 1
    if i == '0':
        if seenq > 0:
            total += (seen1 * pow2 % mod) + (prev * seenq % mod)
            total %= mod
        else:
            total += seen1
            total %= mod\
print(total)
