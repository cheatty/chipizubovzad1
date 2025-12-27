# 1
"""
with open("txt/39762.txt", "r") as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]
    count = 0
    max_sum = 0
    for i in range(len(n) - 1):
        if ((n[i] * n[i + 1]) % 15) == 0 and ((n[i] + n[i + 1]) % 7) == 0:
            count += 1
            if max_sum < (n[i] + n[i + 1]):
                max_sum = (n[i] + n[i + 1])
    print("Количество:", count)
    print("Максимум:", max_sum)
"""
# 2
"""
with open("txt/68279.txt", "r") as f:
    n = [int(el) for el in f]
    max_el = 0

    for el in n:
        if str(el)[-3:] == "562":
            if max_el < el:
                max_el = el

    count = 0
    max_sum = 0
    for i in range(len(n) - 3):
        l = [n[1], n[i + 1], n[i + 2], n[i + 3]]
        l5 = [el for el in l if len(str(el)) == 5]
        lnot5 = [el for el in l if len(str(el)) != 5]
        lcrat3 = [el for el in l if el % 3 == 0]
        lcrat7 = [el for el in l if el % 7 == 0]
        if len(l5) >= 1 and len(lnot5) >= 2:
            if len(lcrat3) < len(lcrat7):
                if sum(l) > max_el and sum(l) < max_el * 2:
                    count += 1
                    if max_sum < sum(l):
                        max_sum = sum(l)
    print("Количество:", count)
    print("Максимум:", max_sum)
"""
# 3
"""
with open("txt/40992.txt", "r") as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]

    count_sredarif = 0
    sum_sredarif = 0

    for el in n:
        if (el % 2) != 0:
            sum_sredarif += el
            count_sredarif += 1

    sredarif = sum_sredarif / count_sredarif

    count = 0
    max_sum = 0

    for i in range(len(n) - 1):
        if (n[i] % 5) == 0 or (n[i + 1] % 5) == 0:
            if n[i] < sredarif or n[i + 1] < sredarif:
                count += 1
                if max_sum < (n[i] + n[i + 1]):
                    max_sum = n[i] + n[i + 1]

    print("Количество:", count)
    print("Максимум:", max_sum)
"""