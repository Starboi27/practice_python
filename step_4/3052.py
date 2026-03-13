a = []
for _ in range(10):
    a.append(int(input()))

result = []
for x in range(10):
    b = a[x] % 42
    if b not in result:
        # list안에 내용 비교는 a in b or a not in b로 하기
        result.append(b)

print(len(result))