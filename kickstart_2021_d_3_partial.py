# Author: Chaudhary Hamdan
# Github link: https://github.com/hamdan-codes


t = int(input())
for iii in range(1, t+1):
    n, m = [int(x) for x in input().split()]
    a, b = [], []
    full_list = []
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        a.append(x)
        b.append(y)
        full_list += list(range(x, y+1))
    s = [int(x) for x in input().split()]
    print('Case #'+str(iii)+':', end=' ')
    for i in range(m):
        diff = 0
        while True:
            val = s[i] - diff
            if val in full_list:
                print(val, end=' ')
                full_list.remove(val)
                break
            val = s[i] + diff
            if val in full_list:
                print(val, end=' ')
                full_list.remove(val)
                break
            diff += 1
    print()
    