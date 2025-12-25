#1

def f(n):
    if len(n) <= 1:
        return n
    if n[0] > n[1]:
        return f(n[1:])
    if n[1] >= n[2]:
        del n[1]
        return f(n)
    return n


arr = [6, 2, 5, 4, 2, 5, 6]
result = f(arr)
print(result)

#2
"""import bisect

def length_of_lis(nums):
    tails = []
    for num in nums:
        i = bisect.bisect_left(tails, num)
        if i == len(tails):
            tails.append(num)
        else:

            tails[i] = num
    return len(tails)

sequence_1 = [6, 2, 5, 4, 2, 5, 6]
result_1 = length_of_lis(sequence_1)
print(sequence_1, result_1)

"""
#3



