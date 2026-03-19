h, m = map(int, input().split())

if (0 <= h <= 23) or (0 <= m <= 59):
    if h == 0:
        if m < 45:
            print("23", m - 45 + 60)
        else:
            print(h, m - 45)
            # 여기에 23를 넣어서 계속 트림
            # 23을 사용한 이유 : 0시을 23시로 바꾸는 데에 집착함
    elif m < 45 and h != 0:
        print(h - 1, m - 45 + 60)
    elif m >= 45:
        print(h, m - 45)
else:
    print("error")

# 45분 보다 적을 때
# 45분 보다 적고 0시 일 때
# 0시일 때
# 0시도 아니고 45분 보다 클 때

"""
if m < 45:
    print(h - 1, m - 45 + 60)
    if h == 0:
        print(h - 1 + 24, m - 45 + 60)
"""
# 처음엔 이 조건을 추가했음 이유는 0시일 때 45분보다 적을 때를 생각 헸음
# 이렇게 구성하면 m < 45:일 때 print와 h == 0:일 때 print가 출력 됨
