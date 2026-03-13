a = int(input())

if 0 < a and 100 < a:
    # 파이썬에선 &&연산자가 아닌 and로 연결한다
    print("error")
elif 90 <= a <= 100:
    print("A")
elif 80 <= a <= 89:
    print("B")
elif 70 <= a <= 79:
    print("C")
elif 60 <= a <= 69:
    print("D")
else:
    print("F")
