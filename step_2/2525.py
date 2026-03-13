h, m = map(int, input().split())
t = int(input())
total = m + t

h = (h + total // 60) % 24
# 24로 나머지를 구한 이유는 23보다 클땐 0으로 시작하기 위해서
m = total % 60

print(h, m)


# %연산은 정수로만 가능 나눗셈에 나머지 연산과 다름
