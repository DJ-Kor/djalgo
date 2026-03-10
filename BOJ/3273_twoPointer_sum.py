# 3273
# 두 수의 합

# 투 포인터 : 양 끝에서 범위를 좁혀가기.

import sys
readl = sys.stdin.readline

N = int(readl())
nums = [int(x) for x in readl().split()]
X = int(readl())

nums.sort()
ans = 0

# set를 이용한 해시 방법
'''
seen = set()

for a in nums:
    if X - a in seen:
        ans += 1
    seen.add(a)
'''

# 정석 방법
p1 = 0
p2 = N - 1

while p1 < p2:
    # print(p1, p2)
    cur = nums[p1] + nums[p2]

    if cur == X:
        # print('ㅁ=>', nums[p1], nums[p2])
        ans += 1
        p1 += 1
        p2 -= 1

    elif cur > X:
        p2 -= 1

    elif cur < X:
        p1 += 1

print(ans)