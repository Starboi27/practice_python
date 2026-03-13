"""
n = int(input())
a = []

for x in range(n):
    a.append(int(input()))
    # append 정수, 리스트, 문자열 등 다양한 요소로 list에 추가가 가능함
    # extend는 튜플, 리스트 등 여러 요소가 포함된 자료형을 풀어서 list에 추가한다

b = int(input())
if b in a:
    print(a.count(b))
else:
    print("입력한 요소가 없음")
"""

n = int(input())
a = list(map(int, input().split()))
v = int(input())
print(a.count(v))