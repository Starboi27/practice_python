a, b = input().split()
# 언패킹으로 리스트 묶음은 해체되고 a, b에 변수가 담긴다

rev_a = a[::-1]
rev_b = b[::-1]
"""
슬라이싱 구조 [start:stop:step]
start : 시작 인덱스
stop : 종료 인덱스
step : 인덱스 증감폭 및 방향
step = 1 : 앞에서 부터 1칸 씩 이동
step = 2 : 앞에서 부터 2칸 씩 이동
step = -1 : 뒤에서 1칸 씩
...

"""

if rev_a > rev_b:
    """
    물자열 이지만 [ㄱ, ㄴ, ㄷ], [a, b, c], [1, 2, 3]
    각각 크기를 사전식 순으로 비교한다
    """
    print(rev_a)
else:
    print(rev_b)