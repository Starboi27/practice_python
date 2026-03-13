a = input().split()
# 첫 시도에는 a=input()만 선언했음 이유는 공백을 상관 안 한 듯?
# 두 번 째엔 공백을 생각하고 split함수를 사용함
sum = 0
# 처음에는 for문 안에 sum=0으로 초기화했음
"""
for i in range(3):
    total = 0              # 매번 0으로 리셋됨!
    total += int(a[i])

# i=0: total=0, total+=1 → 1
# i=1: total=0, total+=2 → 2  ← 다시 0으로!
# i=2: total=0, total+=3 → 3  ← 다시 0으로!
# 최종: 3 (❌ 누적 안 됨!)
"""
# 이런 이유 때문에 밖에서 초기화 한다

for i in range(3):

    sum += int(a[i])

print(sum)
