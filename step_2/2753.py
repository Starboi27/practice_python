a = int(input())

if a < 0 or a > 4000:
    print("error")
elif (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("1")
else:
    print("0")

# 4의 배수는 윤년이다 => a % 4 == 0
# 하지만 100의 배수인 해는 평년이다 => a % 100 != 0
# 두 조건을 종합하면 4의 배수이면서 100의 배수가 아닌 해
# a % 4 == 0 and a % 100 != 0
