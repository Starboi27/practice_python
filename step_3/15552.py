import sys

# sys모듈 : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

a = int(sys.stdin.readline())
# stdin : Standard Input는 buffer라는 임시저장소에 데이터를 뭉텅이로 쌓아두고 한 번에 읽어 온다
# readline : buffer에서 \n(Enter키)를 만날 때 까지 한 줄을 읽음

for x in range(a):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
