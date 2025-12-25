#1
"""
def preobraz(current, target, contains_10=False):
    if current == target:
        return 1 if contains_10 else 0

    if current > target:
        return 0

    programs = 0

    if current + 1 <= target:
        programs += preobraz(current + 1, target, contains_10 or current + 1 == 10)
    if current + 2 <= target:
        programs += preobraz(current + 2, target, contains_10 or current + 2 == 10)
    if current * 2 <= target:
        programs += preobraz(current * 2, target, contains_10 or current * 2 == 10)

    return programs

print(preobraz(3, 12))"""

#2
"""
def preobraz_f(current, target, contains_26=False):
    if current == target:
        return 1

    if current > target or contains_26:
        return 0

    programs = 0
    programs += preobraz_f(current + 1, target, contains_26 or current + 1 == 26)
    programs += preobraz_f(2 * current + 1, target, contains_26 or 2 * current + 1 == 26)

    return programs
print(preobraz_f(1, 27))

"""

#3

def preobraz_s(current, target, contains_9=False, contains_14=False):
    if current == target:
        return 1 if contains_9 and not contains_14 else 0

    if current > target or contains_14:
        return 0

    programs = 0

    programs += preobraz_s(current + 1, target, contains_9 or current + 1 == 9, contains_14 or current + 1 == 14)
    programs += preobraz_s(current + 2, target, contains_9 or current + 2 == 9, contains_14 or current + 2 == 14)

    return programs

print(preobraz_s(2, 18))