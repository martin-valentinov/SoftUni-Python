n = int(input())
m = int(input())
s = int(input())

for address in range(m, n - 1, -1):
    if address == s and address % 2 == 0 and address % 3 == 0:
        break
    elif address % 2 == 0 and address % 3 == 0:
        print(address, end=" ")