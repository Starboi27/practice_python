def cal(a, b) :
    a, b = map(int, input().split())
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)

cal(7, 3)

#map함수는 리스트, 튜플 같은 자료형 데이터에 함수를 적용하여 결과를 돌려주는 함수이다
#map(함수, 자료형 데이터)
#함수는 3가지로 구분 1. def, 2. 파이썬 내장 함수 ex) int, str, floa 3. lamda 함수