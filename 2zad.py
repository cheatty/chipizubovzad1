
#1
"""
l = [0, 1]
n = int(input())

for i in range(n - 2):
    new_el = l[0] + l[1]
    l[0] = l[1]
    l[1] = new_el
    
    print(new_el)
"""
#2
"""
n = int(input())

mas = [0] * (n + 1)

mas[0], mas[1] = 1, 1
for i in range(2, n + 1):
    mas[i] = mas[i - 1] + (mas[i - 2] if i - 2 >= 0 else 0) + (mas[i - 3] if i - 3 >= 0 else 0)
    
print(mas[n])
"""
#3

coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1],
]

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            coins[i][j] = coins[i][j] + coins[i][j-1]
        elif i != 0 and j == 0:
            coins[i][j] = coins[i][j] + coins[i-1][j]
        else:
            coins[i][j] = max(coins[i-1][j], coins[i][j-1]) + coins[i][j]

print(coins[-1][-1])

    
    
    
    
    
    
        

