# 첫 째 줄 N, M N개의 바구니에 M번 공을 교환
# 10810번이랑 비슷함
N, M = map(int, input().split())

arr = list(range(1, N + 1))
"""
처음 시도 땐 arr = [0]*N을 했음
이유는 리스트에 들어있는 값을 신경안 쓴 듯?
이 문제는 각 리스트에 1~N 값이 들어있는걸
i에서 j로 j에서 i로 위치 바꾸는 건데
처음 시도 일단 N개의 리스트에 있는 값을
for문에 추가해서 위치 바꾸는 걸 시도함.
"""
for _ in range(M):
    i, j = map(int, input().split())
    temp = arr[i - 1]
    arr[i - 1] = arr[j - 1]
    arr[j - 1] = temp
    """
    파이썬에선 다중할당이런 기능을 사용하여 임시변수 없이 위치 변경 가능
    a, b = b, a
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]
    """
print(*arr)
