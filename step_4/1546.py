n = int(input())
arr = list(map(float, input().split()))[:n]
# [:n] : 생성된 리스트에 인덱스 0부터 n-1 요소만 저장한다

total = 0
for x in arr:
    total += (x / max(arr)) * 100

print(total / n)
