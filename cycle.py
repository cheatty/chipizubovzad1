#1
"""
for num in range(15):
    a = list(reversed([1, 2, 3, num, 5, 1, 5]))
    b = list(reversed([1, num, 2, 3, 3, 1, 5]))

    for i in range(7):
        a[i] = a[i] * 15 ** i
        b[i] = b[i] * 15 ** i

    if (sum(a) + sum(b)) % 14 == 0:
        print((sum(a) + sum(b)) // 14)
        break
"""

#3
"""
for x in range(10):
    n1 = x * 17**3 + 11 * 17**2 + 0 * 17**1 + 9 * 17**0
    n2 = x * 15**3 + 8 * 15**2 + 14 * 15**1 + 8 * 15**0
    res = n1 + n2
    if res % 155 == 0:
        print(res // 155)
        break
"""
#4
"""
for x in range(8):
    for y in range(8):
        if x <= 7 and y <= 7:
            num11 = int(str(y) + '04' + str(x) + '5', 11)
            num8 = int('253' + str(x) + str(y), 8)
            total = num11 + num8
            if total % 117 == 0:
                print(total // 117)
                break
    else:
        continue
    break
"""
#5
"""
expression_value = 7 * (8**3)**1912 + 6 * (8**2)**1954 - 5 * (8**1991) - 4 * (8**1980) - 2022

def count_sevens_in_base8(n):
    count = 0
    if n == 0:
        return 0
    while n > 0:
        if n % 8 == 7:
            count += 1
        n //= 8
    return count

sevens_count = count_sevens_in_base8(expression_value)
print(sevens_count)
"""