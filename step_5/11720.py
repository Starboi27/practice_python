n = int(input())

arr = list(map(int, input()))

sum = 0
for x in range(n):
    sum += arr[x]

print(sum)

"""
a = input()
b = input()
s = 0
for i in b:
b에 저장된 예를 들어 54321이라 하면
i는 5~1까지 호출 됨
    s += int(i)
print(s)
"""
