check = [0, 0] + [1] * 100

print(check)


for i in range(len(check)):
    if check[i]:
        print(i, end=' ')
        for j in range(i * 2, len(check), i):
            check[j] = 0

print()
print('Process Done')
print(check)
