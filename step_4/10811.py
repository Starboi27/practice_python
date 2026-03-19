"""
[] = 1, 2, 3, 4, 5
1) 2, 1, 3, 4, 5
2) 2, 1, 4, 3, 5
3) 3, 4, 1, 2, 5
2번 째 줄은 범위를 나타낸다
"""

n, m = map(int, input().split())
arr = list(range(1, n + 1))

for x in range(m):
    i, j = map(int, input().split())
    arr[i - 1 : j] = arr[i - 1 : j][::-1]
    """
    arr[i - 1 : j] 변경할 리스트의 범위를 지정하고
    arr[i - 1 : j] 역순으로 만들 데이터를 해당 범위에서 가져온다
    [::-1]는 슬라이싱 문법이다 [start:stop:step]의 형식을 가지며
    start : 복사를 시작할 인덱스
    stop : 복사를 마칠 인덱스
    step : 데이터를 추출할 간격
    위 3가지 기본 구조를 나타낸다
    """
print(arr)
