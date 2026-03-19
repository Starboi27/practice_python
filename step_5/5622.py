# 1을 걸려면 2초가 필요함
# 만약 3을 걸려면 4초가 필요함
# N+1초가 필요함
# WA = 13s
# UNUCIC = 36s
# (U=9:2), (N=7:1), (C=3:2), (I=5:1)
# 18 + 7 + 6 + 5 = 36

dial = {
    "ABC": 3,
    "DEF": 4,
    "GHI": 5,
    "JKL": 6,
    "MNO": 7,
    "PQRS": 8,
    "TUV": 9,
    "WXYZ": 10,
}

s = input()
sum = 0

for char in s:
    """
    입력 받은 문자열을 분리해 하나씩 탐색
    ex) UV를 입력했다면 첫번 째 반복에 U를 분리하여 char 변수에 넣음
    """
    for key in dial:
        # dial 딕셔너리에 있는 key 값을 key변수에 넣음
        if char in key:
            """
            key 변수에 담긴 key 값이랑 char에 담긴 U랑 비교
            U == "TUV" 일 때 if문 실행
            """
            sum += dial[key]

print(sum)
